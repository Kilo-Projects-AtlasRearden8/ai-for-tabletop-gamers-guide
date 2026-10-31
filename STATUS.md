# STATUS

## What was built

A beginner manual and static website for using free AI with tabletop RPGs and
board games, published by **Asdale Dynamics, LLC**.

### Manual (`docs/`)
Eleven Markdown documents:

1. `00-intro.md` — welcome, scope, what the guide does and does not do
2. `01-getting-started.md` — picking a free AI tool, account setup, first chat,
   first prompt, what to avoid
3. `02-character-sheets.md` — story-first character creation prompts and tips
4. `03-campaign-notes.md` — session summaries, organizing messy notes, privacy
5. `04-npc-ideas.md` — one NPC and three-NPC brainstorming prompts
6. `05-rule-clarifications.md` — explain/compare rule prompts, plus warnings
   that AI is not a rulebook
7. `06-session-prep.md` — session and encounter planning prompts, prep checklist
8. `07-printable-worksheets.md` — the two worksheets and how to print them
9. `08-step-by-step-prompts.md` — every prompt from the guide, copy-and-paste
10. `09-privacy-and-safety.md` — privacy rules, education-only notice,
    copyright respect
11. `10-faq.md` — frequently asked questions

### Static site (`site/`)
Thirteen HTML pages mirroring the manual, shared `site/assets/style.css` and
`site/assets/print.css`, plus printable worksheets:

- `site/index.html` — home
- `site/getting-started.html` … `site/faq.html` — one page per manual section
- `site/worksheets/character-sheet.html` — one-page fill-in character sheet
- `site/worksheets/session-worksheet.html` — session prep + rule-questions sheet

### Other files
- `LICENSE` — MIT License, copyright line exactly
  `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — project overview with Asdale Dynamics, LLC credit
- `verify.py` — verification script (see results below)

## How to run it

No install, no server, no account is needed to read the guide.

1. Open `site/index.html` in any web browser, or read `docs/00-intro.md`.
2. Worksheets: open `site/worksheets/character-sheet.html` or
   `site/worksheets/session-worksheet.html`, then print (Ctrl+P / Command+P).
   Print styles hide navigation and color so they print cleanly on plain paper.

To run the verification script:

```
python3 verify.py
```

## Verification results

`python3 verify.py` — all checks pass:

- 29 required files exist
- `LICENSE` contains the exact line `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` credits Asdale Dynamics, LLC
- All 13 HTML files parse and every internal link resolves
- Each site page has a matching docs markdown file (or is the home page / a
  worksheet)
- Secret scan of 29 files found no API keys, tokens, or private keys

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
