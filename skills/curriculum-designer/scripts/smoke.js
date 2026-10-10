// Smoke test for a built course page. Usage: node smoke.js <built.html>
// Requires `playwright` in node_modules (npm i playwright) and the system Chromium.
const { chromium } = require('playwright');
const fs = require('fs');
const file = process.argv[2];
if (!file) { console.error('usage: node smoke.js <built.html>'); process.exit(2); }
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM || '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
  const errs = [], fails = [];
  const check = (ok, msg) => { console.log((ok ? 'ok   ' : 'FAIL ') + msg); if (!ok) fails.push(msg); };
  p.on('pageerror', e => errs.push(e.message));
  const html = fs.readFileSync(file, 'utf8');
  await p.setContent('<!doctype html><html><head><meta charset="utf-8"></head><body>' + html + '</body></html>');
  const go = async h => { await p.evaluate(h => { location.hash = h; }, h); await p.waitForTimeout(150); };
  const nMod = await p.evaluate(() => JSON.parse(document.getElementById("course-data").textContent).modules.length);
  const views = ['home', ...Array.from({ length: nMod }, (_, i) => 'm' + i), 'cards', 'brief', 'model', 'tensions', 'cases', 'diagnostic'];
  for (const v of views) {
    await go(v);
    const t = await p.evaluate(() => document.querySelector('main h1')?.textContent || '');
    const w = await p.evaluate(() => document.documentElement.scrollWidth);
    check(t.length > 0 && w <= 1280, `view ${v} renders h1 "${t.slice(0, 50)}" width ${w}`);
  }
  await go('m1'); await p.click('.opt'); await p.waitForTimeout(100);
  check(await p.$('.diag') !== null, 'hinge question shows a diagnosis');
  await p.click('#doneBtn'); await go('cards');
  const hasCard = await p.$('#flip');
  check(!!hasCard, 'cards unlock after completing m1');
  if (hasCard) { await p.click('#flip'); await p.click('[data-g="2"]'); check(true, 'card graded'); }
  await go('brief'); await p.click('[data-add]');
  check((await p.$$('.entry')).length >= 1, 'brief entry added');
  await go('cases'); await p.click('[data-case]'); await p.click('#reveal');
  check((await p.$$('.step.reveal')).length >= 1, 'case reveals model answer');
  await go('model'); await p.click('[data-node]');
  check((await p.$$('.band .panel')).length >= 1, 'model node panel opens');
  await go('diagnostic');
  check(await p.$('main') !== null, 'diagnostic view');
  await p.setViewportSize({ width: 390, height: 800 });
  for (const v of ['home', 'm2', 'tensions', 'brief', 'cards']) { await go(v); const w = await p.evaluate(() => document.documentElement.scrollWidth); check(w <= 390, `mobile ${v} no horizontal overflow (${w})`); }
  check(errs.length === 0, 'no page errors ' + JSON.stringify(errs));
  await b.close();
  console.log(fails.length ? `\n${fails.length} FAILURES` : '\nALL PASS');
  process.exit(fails.length ? 1 : 0);
})();
