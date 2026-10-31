# STATUS

## What was built

A beginner manual and static website for using free AI with tabletop RPGs and
board games, published by **Asdale Dynamics, LLC**.

### Manual (`docs/`) — twelve documents

1. `00-intro.md` — Welcome, scope, what the guide does and does not do
2. `01-getting-started.md` — Picking a free AI tool, account setup, first chat,
   first prompt, what to avoid
3. `02-character-sheets.md` — Story-first character creation prompts and tips
4. `03-campaign-notes.md` — Session summaries, organizing messy notes, privacy
5. `04-npc-ideas.md` — One NPC and three-NPC brainstorming prompts
6. `05-rule-clarifications.md` — Explain/compare rule prompts, plus warnings
   that AI is not a rulebook
7. `06-session-prep.md` — Session and encounter planning prompts, prep checklist
8. `07-printable-worksheets.md` — The two worksheets and how to print them
9. `08-step-by-step-prompts.md` — Every prompt from the guide, copy and paste
10. `09-privacy-and-safety.md` — Privacy rules, education-only notice,
    copyright respect
11. `10-faq.md` — Frequently asked questions
12. `11-board-games.md` — Using AI with board games: rule explanations,
    teaching new players, setup/teardown checklist, solo/variant ideas,
    scorekeeping help

### Static site (`site/`) — fourteen HTML pages

Thirteen content pages mirroring the manual plus `site/board-games.html`,
shared `site/assets/style.css` and `site/assets/print.css`, and two printable
worksheets:

- `site/index.html` — Home
- `site/getting-started.html` … `site/board-games.html` — one page per section
- `site/worksheets/character-sheet.html` — one-page fill-in character sheet
- `site/worksheets/session-worksheet.html` — session prep + rule questions sheet
  (also usable for board games)

### Other files
- `LICENSE` — MIT License, copyright line exactly
  `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — project overview with Asdale Dynamics, LLC credit and a full
  table of contents
- `verify.py` — verification script (see results below)

## How to run it

No install, no server, no account is needed to read the guide.

1. Open `site/index.html` in any web browser, or read `docs/00-intro.md`.
2. Worksheets: open `site/worksheets/character-sheet.html` or
   `site/worksheets/session-worksheet.html`, then print (Ctrl+P / Command+P).
   Print styles hide menus and colors so they print clearly on plain paper.

To run the verification script:

```
python3 verify.py
```

## Verification results

`python3 verify.py` — all checks pass:

- 31 required files exist
- `LICENSE` contains the exact line `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` credits Asdale Dynamics, LLC
- All 14 HTML files parse and every internal link resolves
- Each site page has a matching docs markdown file (or is the home page / a
  worksheet)
- Secret scan of 32 files found no API keys, tokens, or private keys
- Total: 280 checks, 0 failures

## Known gaps

- No automated build step or test framework: the site is plain HTML/Markdown
  that opens directly in a browser; verification is the `verify.py` script.
- No live AI integration: this is an education-only guide with prompts the user
  pastes into their own free AI tool; nothing here calls an AI service.
- Print layout tested by inspection of CSS (`@page`, print media query), not by
  an actual printer.
- No game assets, stat blocks, monsters, or rules text included by design.
- No remote repository, no GitHub Actions workflows, nothing pushed or
  published.
- The guide is RPG-first with a smaller board games section; board game content
  could be expanded further if desired.
