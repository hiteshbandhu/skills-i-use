# Research Report

Deep research on a new technology paradigm — what it is, how it is built, who sells it, and
where it fits in your own product — delivered as a visual PDF the team can read and share.

Output: `./skill-outputs/research-report/`

## Why

A new trend arrives as a product launch and a wave of hot takes. To decide whether to adopt
it you need three answers in one place: how the thing actually works, which providers you
could buy it from (with real prices), and where it would land in your own codebase. This
skill produces all three, sourced, with every number charted.

## How it works

1. Five parallel researchers: products & philosophy, architecture, two provider groups, and a
   read-only pass over your codebase. Uses a deep-research skill when installed; otherwise
   plain subagents.
2. A report writer turns the notes into one report: executive summary, three sections,
   caveats and sources. Nothing appears twice.
3. The [`pdf-report`](../pdf-report/) skill renders it with charts and diagrams.
4. Every page is rendered to an image and checked before delivery ([verify.md](verify.md)).

## What is in here

| File | Contents |
|---|---|
| [SKILL.md](SKILL.md) | The brief, the duplication rule, the five-step process |
| [verify.md](verify.md) | Page-by-page check and the traps of long chart-heavy PDFs |

## Install

```bash
npx skills add hiteshbandhu/skills-i-use --skill research-report
npx skills add hiteshbandhu/skills-i-use --skill pdf-report   # renderer it depends on
```

Or copy the folder into `~/.claude/skills/` or `~/.cursor/skills/`.

## Usage

```
/research-report always-on sandboxes; products: Grok Bot, ChatGPT dots; providers: DigitalOcean, Daytona
```

Requires headless Chrome and `poppler` (`pdftoppm`, `pdftotext`) for rendering and checks.
