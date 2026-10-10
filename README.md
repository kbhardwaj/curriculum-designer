# curriculum-designer

An agent skill that turns a topic or a reading list into a self-paced course you can actually work through. It made both courses on [twocents.page](https://twocents.page/paths/): Founding School (13 books on learning and school design) and Games and Norms (11 books on why people cooperate).

Give it a subject, or a list of books and papers. It breaks down each source, works out where they agree and disagree, and builds a single-page course app with:

- a question to try before each lesson;
- quizzes where every wrong answer tells you which misconception you hold;
- review cards on a spaced schedule;
- a working brief you build up module by module, and a final project.

## Install

In Claude Code:

```
/plugin marketplace add kbhardwaj/curriculum-designer
/plugin install curriculum-designer@kbhardwaj
```

Without the plugin system, copy the skill folder into your personal skills:

```
git clone https://github.com/kbhardwaj/curriculum-designer
cp -r curriculum-designer/skills/curriculum-designer ~/.claude/skills/
```

The skill is plain Markdown plus a few Python scripts, so other agents that read `SKILL.md` files can use the same folder.

## Use

```
/curriculum-designer "game theory and social norms" --sources books.txt --goal "write a cooperation plan for my team"
```

A standard run takes a while and uses a lot of tokens: one subagent per source, then several synthesis passes. Start with `--depth light` to see the shape.

## Requirements

- Python 3 for `app/build.py` and `scripts/validate.py`.
- Node and Playwright, only for the optional smoke test.
- The in-course mentor needs a model. On claude.ai it uses yours. To self-host it, run `scripts/mentor_proxy.py` behind your own auth with your own API key.

## What it won't do

It's told not to make up studies or numbers, and every book file says how its contents were checked. It can still be wrong. Spot-check the claims you plan to rely on.

## License

MIT
