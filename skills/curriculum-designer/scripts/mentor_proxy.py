#!/usr/bin/env python3
"""Minimal mentor endpoint for a self-hosted course page.

The standalone page (build.py --standalone --mentor-endpoint http://host:port/mentor) POSTs
{"prompt": "..."} here and renders the plain-text stream it gets back. This server adds nothing
to the prompt: the page already includes the mentor voice and the learner's work.

Run:  pip install anthropic && ANTHROPIC_API_KEY=... python3 mentor_proxy.py [--port 8787] [--origin https://your.site]
Credentials resolve the way the SDK does (ANTHROPIC_API_KEY, ANTHROPIC_AUTH_TOKEN or an `ant auth login` profile).

Put it behind your own auth if the page is public: every request costs API tokens.
"""
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import anthropic

MODEL = "claude-opus-5-5"
MAX_PROMPT_CHARS = 60_000
client = anthropic.Anthropic()
ORIGIN = "*"


class Handler(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", ORIGIN)
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_POST(self):
        if self.path != "/mentor":
            self.send_response(404); self.end_headers(); return
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
            prompt = str(body.get("prompt", ""))[:MAX_PROMPT_CHARS]
        except (ValueError, TypeError):
            self.send_response(400); self.end_headers(); return
        if not prompt.strip():
            self.send_response(400); self.end_headers(); return
        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Accel-Buffering", "no")
        self.end_headers()
        try:
            with client.messages.stream(
                model=MODEL,
                max_tokens=4096,
                output_config={"effort": "medium"},
                messages=[{"role": "user", "content": prompt}],
            ) as stream:
                for text in stream.text_stream:
                    self.wfile.write(text.encode("utf-8"))
                    self.wfile.flush()
                final = stream.get_final_message()
                if final.stop_reason == "refusal":
                    self.wfile.write("\n\n(The mentor declined to answer this one.)".encode("utf-8"))
        except anthropic.RateLimitError:
            self.wfile.write("\n\n(Rate limited; try again in a minute.)".encode("utf-8"))
        except anthropic.APIStatusError as e:
            self.wfile.write(f"\n\n(API error {e.status_code}.)".encode("utf-8"))
        except anthropic.APIConnectionError:
            self.wfile.write("\n\n(Could not reach the API.)".encode("utf-8"))
        except (BrokenPipeError, ConnectionResetError):
            pass

    def log_message(self, fmt, *args):  # quieter default log
        print("%s - %s" % (self.address_string(), fmt % args))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8787)
    ap.add_argument("--origin", default="*", help="Access-Control-Allow-Origin value, e.g. https://your.site")
    a = ap.parse_args()
    ORIGIN = a.origin
    print(f"mentor proxy on http://127.0.0.1:{a.port}/mentor (model {MODEL})")
    ThreadingHTTPServer(("0.0.0.0", a.port), Handler).serve_forever()
