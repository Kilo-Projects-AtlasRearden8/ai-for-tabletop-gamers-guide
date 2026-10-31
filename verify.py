#!/usr/bin/env python3
"""Verification script for the AI for Tabletop RPGs and Board Games guide.

Checks:
  - Required files exist
  - LICENSE has the exact copyright line
  - README credits Asdale Dynamics, LLC
  - Every HTML file parses
  - Internal links and asset references resolve
  - No secret-like patterns in any tracked file
  - Docs markdown files exist for each site page

Run: python3 verify.py
"""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent

DOCS = [
    "docs/00-intro.md",
    "docs/01-getting-started.md",
    "docs/02-character-sheets.md",
    "docs/03-campaign-notes.md",
    "docs/04-npc-ideas.md",
    "docs/05-rule-clarifications.md",
    "docs/06-session-prep.md",
    "docs/07-printable-worksheets.md",
    "docs/08-step-by-step-prompts.md",
    "docs/09-privacy-and-safety.md",
    "docs/10-faq.md",
    "docs/11-board-games.md",
]

SITE_PAGES = [
    "site/index.html",
    "site/getting-started.html",
    "site/character-sheets.html",
    "site/campaign-notes.html",
    "site/npc-ideas.html",
    "site/rule-clarifications.html",
    "site/session-prep.html",
    "site/printable-worksheets.html",
    "site/step-by-step-prompts.html",
    "site/board-games.html",
    "site/privacy-and-safety.html",
    "site/faq.html",
    "site/worksheets/character-sheet.html",
    "site/worksheets/session-worksheet.html",
]

ASSETS = [
    "site/assets/style.css",
    "site/assets/print.css",
]

REQUIRED_FILES = ["LICENSE", "README.md", "STATUS.md"] + DOCS + SITE_PAGES + ASSETS

EXACT_COPYRIGHT = "Copyright (c) 2026 Asdale Dynamics, LLC"

# Patterns that would indicate an actual secret (not just the word in prose).
SECRET_PATTERNS = [
    re.compile(r"\bsk-[A-Za-z0-9]{20,}"),          # OpenAI-style keys
    re.compile(r"\bghp_[A-Za-z0-9]{20,}"),          # GitHub tokens
    re.compile(r"\bAKIA[0-9A-Z]{16}"),              # AWS keys
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),  # private keys
    re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"]?[A-Za-z0-9_-]{16,}"),
    re.compile(r"(?i)secret\s*[:=]\s*['\"]?[A-Za-z0-9_-]{16,}"),
]


class LinkChecker(HTMLParser):
    """Collects href/src attributes from HTML."""

    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for attr, value in attrs:
            if attr in ("href", "src") and value:
                self.links.append(value)


failures = []
checks = 0


def check(condition, message):
    global checks
    checks += 1
    if condition:
        print(f"  ok   {message}")
    else:
        failures.append(message)
        print(f"  FAIL {message}")


def main():
    print(f"Root: {ROOT}\n")

    # 1. Required files exist
    print(f"== {len(REQUIRED_FILES)} required files ==")
    for rel in REQUIRED_FILES:
        check((ROOT / rel).is_file(), f"{rel} exists")

    # 2. LICENSE exact copyright line
    print("\n== LICENSE copyright line ==")
    license_text = (ROOT / "LICENSE").read_text()
    check(EXACT_COPYRIGHT in license_text.splitlines(),
          f"LICENSE contains exact line: {EXACT_COPYRIGHT!r}")

    # 3. README credits
    print("\n== README credit ==")
    readme_text = (ROOT / "README.md").read_text()
    check("Asdale Dynamics, LLC" in readme_text,
          "README mentions Asdale Dynamics, LLC")

    # 4. HTML parsing
    print(f"\n== {len(SITE_PAGES)} HTML files parse ==")
    for rel in SITE_PAGES:
        path = ROOT / rel
        text = path.read_text()
        parser = LinkChecker()
        try:
            parser.feed(text)
            check(True, f"{rel} parses as HTML")
        except Exception as exc:  # pragma: no cover - html.parser rarely raises
            check(False, f"{rel} parse error: {exc}")

        # 5. Internal links resolve
        base = path.parent
        for link in parser.links:
            if link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = (base / link).resolve()
            check(target.is_file(), f"{rel}: link -> {link} resolves")

    # 6. Docs markdown referenced by site pages exist
    print("\n== Docs backing each site page ==")
    for rel in SITE_PAGES:
        page = Path(rel).stem
        # worksheet pages don't have a dedicated doc; check docs directory generally
        candidates = [d for d in DOCS if page in Path(d).stem or Path(d).stem in page]
        if candidates:
            check(all((ROOT / d).is_file() for d in candidates),
                  f"{rel} has docs backup: {', '.join(candidates)}")
        else:
            check(page in ("index", "character-sheet", "session-worksheet"),
                  f"{rel} is home or a worksheet (no dedicated doc expected)")

    # 7. No secrets anywhere
    print("\n== Secret scan ==")
    scanned = 0
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(errors="ignore")
        except Exception:
            continue
        scanned += 1
        for pattern in SECRET_PATTERNS:
            for match in pattern.finditer(text):
                failures.append(f"{path}: possible secret {match.group(0)!r}")
    check(len(failures) == 0 or not any("possible secret" in f for f in failures),
          f"{scanned} files scanned, no secrets found")

    print(f"\n== Summary: {checks} checks, {len(failures)} failure(s) ==")
    for failure in failures:
        print(f"  - {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
