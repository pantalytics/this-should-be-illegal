#!/usr/bin/env python3
"""Flag templates whose cited articles changed since `last_checked`.

Uses the git history of wetgeving-nl (Dutch law as Markdown, CC0): for each article in a
template's `legal_basis`, compare its text on the `last_checked` date with today's text.

Usage: python scripts/check_law.py     (set GITHUB_TOKEN to avoid API rate limits)
Exit code 1 when an article changed or could not be found.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
from functools import cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate import ROOT, load_frontmatter, template_files  # noqa: E402

REPO = "Apolloccrypt/wetgeving-nl"
# Law code in `legal_basis` -> file in wetgeving-nl. Extend when templates cite new laws.
LAWS = {
    **{f"BW {n}": f"wetten/burgerlijk-recht/burgerlijk-wetboek-boek-{n}.md" for n in "1234567"},
    "Wet IB 2001": "wetten/belastingrecht/wet-inkomstenbelasting-2001.md",
}


def get(url: str) -> str:
    headers = {"User-Agent": "this-should-be-illegal"}
    if url.startswith("https://api.github.com") and os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as r:
        return r.read().decode("utf-8")


@cache
def law_text(path: str, until: str | None) -> str:
    ref = "main"
    if until:
        commits = json.loads(get(
            f"https://api.github.com/repos/{REPO}/commits?path={path}&until={until}T23:59:59Z&per_page=1"
        ))
        if not commits:
            raise LookupError(f"no version of {path} on or before {until}")
        ref = commits[0]["sha"]
    return get(f"https://raw.githubusercontent.com/{REPO}/{ref}/{path}")


def article(text: str, number: str) -> str:
    m = re.search(rf"^#+ Artikel {re.escape(number)}\b\.?[^\n]*\n(.*?)(?=^#+ |\Z)", text, re.S | re.M)
    if not m:
        raise LookupError(f"Artikel {number} not found")
    body = re.sub(r"&[zg]=\d{4}-\d{2}-\d{2}", "", m[1])  # link date stamps change daily
    return re.sub(r"\s+", " ", body).strip()


def split(ref: str) -> tuple[str, str]:
    m = re.match(r"^(BW \d+):(\S+)$", ref) or re.match(r"^(.+) (\S+)$", ref)
    if not m or m[1] not in LAWS:
        raise LookupError(f"unknown law in `{ref}`; add it to LAWS in scripts/check_law.py")
    return LAWS[m[1]], m[2]


def main() -> int:
    problems = 0
    for path in template_files():
        meta = load_frontmatter(path)
        checked = str(meta["last_checked"])
        for ref in meta["legal_basis"]:
            try:
                file, number = split(ref)
                changed = article(law_text(file, checked), number) != article(law_text(file, None), number)
            except LookupError as exc:
                print(f"::error file={path.relative_to(ROOT)}::{ref}: {exc}")
                problems += 1
                continue
            if changed:
                print(f"::error file={path.relative_to(ROOT)}::{ref} changed since {checked}")
                problems += 1
            else:
                print(f"ok  {path.name}: {ref}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
