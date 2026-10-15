#!/usr/bin/env python3
"""Render every template to ready-to-use Markdown and Word files in dist/.

- frontmatter becomes a short header (version, status, disclaimer);
- {{placeholders}} become visible fill-in markers with the suggested value;
- option markers are dropped, all options stay visible so the user can pick;
- the legal basis becomes a list of links to the current law text.

Needs pandoc for the .docx files. Usage: python scripts/build.py
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_law_changes import article_url  # noqa: E402
from validate import ROOT, body, load_frontmatter, template_files  # noqa: E402

DIST = ROOT / "dist"
PLACEHOLDER = re.compile(r"\{\{\s*([a-z0-9_]+)\s*\}\}")
MARKER = re.compile(r"^<!-- /?optie[^>]*-->\n", re.M)


def fill_marker(spec: str | dict, highlight: bool) -> str:
    """Visible fill-in marker; highlighted in Word via pandoc's `mark` span."""
    if isinstance(spec, str):
        spec = {"label": spec}
    hint = f", bijv. {spec['suggestie']}" if spec.get("suggestie") else ""
    marker = f"[● {spec['label']}{hint}]"
    return f"[{marker}]{{.mark}}" if highlight else marker


def law_label(ref: str) -> str:
    return "art. " + ref.removeprefix("BW ") + " BW"


def render(path: Path, highlight: bool = False) -> str:
    meta = load_frontmatter(path)
    fields = meta["fields"]
    text = MARKER.sub("", body(path))
    text = PLACEHOLDER.sub(lambda m: fill_marker(fields[m[1]], highlight), text)
    reviewed = (
        f"beoordeeld door {meta['reviewed_by']}"
        if meta["status"] == "reviewed"
        else "concept, nog niet beoordeeld door een advocaat"
    )
    header = (
        f"> Versie {meta['version']}, {reviewed}, gecontroleerd op {meta['last_checked']}. "
        "Geen juridisch advies. Bron en nieuwste versie: "
        "<https://github.com/pantalytics/this-should-be-illegal>\n\n"
    )
    laws = "\n".join(f"- [{law_label(ref)}]({article_url(ref)})" for ref in meta["legal_basis"])
    footer = f"\n\n## Wettelijke grondslag\n\n{laws}\n\nLicentie: CC BY 4.0, Pantalytics en bijdragers.\n"
    return header + text.strip() + footer


def main() -> int:
    if DIST.exists():
        shutil.rmtree(DIST)
    pandoc = shutil.which("pandoc")
    for path in template_files():
        rel = path.relative_to(ROOT / "plugins")
        country = rel.parts[0].removeprefix("legal-")
        out = DIST / country / path.stem
        out.parent.mkdir(parents=True, exist_ok=True)
        md = out.with_suffix(".md")
        md.write_text(render(path), encoding="utf-8")
        if pandoc:
            subprocess.run(
                [pandoc, "-f", "markdown-yaml_metadata_block+mark", "-o", str(out.with_suffix(".docx"))],
                input=render(path, highlight=True), text=True, check=True,
            )
        print(f"built {md.relative_to(ROOT)}{' + .docx' if pandoc else ''}")
    if not pandoc:
        print("pandoc not found: skipped .docx", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
