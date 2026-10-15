#!/usr/bin/env python3
"""Flag templates whose cited articles changed after the template was last checked.

Every template lists its legal basis in frontmatter, e.g. ``BW 2:238``. This
script looks up the current version of each article on wetten.overheid.nl and
compares its "in werking getreden" date with the template's ``last_checked``.
A newer article version means the template must be re-checked by a human.

Usage: python scripts/check_law_changes.py [paths...]
Exit code 1 when at least one template is stale.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate import load_frontmatter, template_files  # noqa: E402

# Code -> wetten.overheid.nl BWB id. Extend when templates cite new laws.
BWB_IDS = {
    "BW 2": "BWBR0003045",
    "BW 3": "BWBR0005291",
    "BW 6": "BWBR0005289",
    "BW 7": "BWBR0005290",
}
REF = re.compile(r"^(?P<code>BW \d+):(?P<article>\d+[a-z]?)$")
_cache: dict[str, str] = {}


def fetch(bwb_id: str) -> str:
    if bwb_id not in _cache:
        req = urllib.request.Request(
            f"https://wetten.overheid.nl/{bwb_id}",
            headers={"User-Agent": "this-should-be-illegal law-check"},
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            _cache[bwb_id] = resp.read().decode("utf-8", errors="ignore")
    return _cache[bwb_id]


def lookup(ref: str) -> tuple[str, dt.date]:
    """Return (anchor id, in-force date) of the current version of an article."""
    m = REF.match(ref)
    if not m:
        raise ValueError(f"unsupported legal_basis format: {ref!r}")
    bwb_id = BWB_IDS[m["code"]]
    hit = re.search(
        rf'id="([A-Za-z0-9_]+_Artikel{m["article"]})" data-bwb-id="{bwb_id}" '
        rf'data-iwt-datum="(\d{{4}}-\d{{2}}-\d{{2}})"',
        fetch(bwb_id),
    )
    if not hit:
        raise LookupError(f"{ref} not found on wetten.overheid.nl ({bwb_id})")
    return hit[1], dt.date.fromisoformat(hit[2])


def article_date(ref: str) -> dt.date:
    return lookup(ref)[1]


def article_url(ref: str) -> str:
    """Link to the always-current version of the article."""
    anchor, _ = lookup(ref)
    return f"https://wetten.overheid.nl/{BWB_IDS[REF.match(ref)['code']]}/#{anchor}"


def main(paths: list[str]) -> int:
    stale = 0
    for path in template_files(paths):
        meta = load_frontmatter(path)
        checked = dt.date.fromisoformat(str(meta["last_checked"]))
        for ref in meta["legal_basis"]:
            try:
                changed = article_date(ref)
            except (LookupError, ValueError) as exc:
                print(f"::error file={path}::{exc}")
                stale += 1
                continue
            if changed > checked:
                print(f"::error file={path}::{ref} changed on {changed}, template last checked {checked}")
                stale += 1
            else:
                print(f"ok  {path}: {ref} (version {changed})")
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
