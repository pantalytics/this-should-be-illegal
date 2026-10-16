#!/usr/bin/env python3
"""Structural checks for templates, skills and the plugin marketplace.

Runs offline, no dependencies beyond PyYAML. Fails CI when:
- a template misses required frontmatter or cites no legal basis
- a {{placeholder}} in the body is not declared in `fields`, or vice versa
- a template marked `reviewed` has no `reviewed_by`
- `last_checked` is older than MAX_AGE_DAYS
- a skill's SKILL.md misses name/description or the name does not match its folder
- a marketplace plugin source or plugin.json is missing
- a file is not Markdown/plain text, or carries a license other than MIT or CC BY 4.0
"""

from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MAX_AGE_DAYS = 365
REQUIRED = ["title", "jurisdiction", "language", "version", "status", "last_checked", "legal_basis", "fields"]
STATUSES = {"draft", "reviewed"}
PLACEHOLDER = re.compile(r"\{\{\s*([a-z0-9_]+)\s*\}\}")
OPTION_BLOCK = re.compile(r"<!-- optie ([a-z0-9_]+)=([a-z]) -->\n(.*?)\n<!-- /optie -->", re.S)
OPTION_MARKER = re.compile(r"^<!-- /?optie\b", re.M)

errors: list[str] = []


def error(path: Path, msg: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {msg}")


def load_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise ValueError(f"{path}: missing YAML frontmatter")
    return yaml.safe_load(m[1]) or {}


def body(path: Path) -> str:
    return re.sub(r"^---\n.*?\n---\n", "", path.read_text(encoding="utf-8"), count=1, flags=re.S)


def template_files(paths: list[str] | None = None) -> list[Path]:
    if paths:
        return [Path(p).resolve() for p in paths]
    return sorted(p for p in ROOT.glob("plugins/*/templates/**/*.md") if p.name != "README.md")


def check_template(path: Path) -> None:
    try:
        meta = load_frontmatter(path)
    except ValueError as exc:
        error(path, str(exc))
        return
    for key in REQUIRED:
        if key not in meta:
            error(path, f"missing frontmatter key `{key}`")
    if meta.get("status") not in STATUSES:
        error(path, f"status must be one of {sorted(STATUSES)}")
    if meta.get("status") == "reviewed" and not meta.get("reviewed_by"):
        error(path, "status `reviewed` requires `reviewed_by` (name + role, e.g. advocaat)")
    if not meta.get("legal_basis"):
        error(path, "`legal_basis` must cite at least one article")
    checked = meta.get("last_checked")
    if checked:
        age = (dt.date.today() - dt.date.fromisoformat(str(checked))).days
        if age > MAX_AGE_DAYS:
            error(path, f"last_checked is {age} days old (max {MAX_AGE_DAYS}); re-check against current law")
    fields = meta.get("fields") or {}
    for name, spec in fields.items():
        if isinstance(spec, dict) and not spec.get("label"):
            error(path, f"field `{name}` needs a `label`")
        elif not isinstance(spec, (str, dict)):
            error(path, f"field `{name}` must be a label or a mapping with label/suggestie")
    text = body(path)
    used = set(PLACEHOLDER.findall(text))
    for name in sorted(used - set(fields)):
        error(path, f"placeholder `{{{{{name}}}}}` used but not declared in `fields`")
    for name in sorted(set(fields) - used):
        error(path, f"field `{name}` declared but never used")
    check_options(path, meta.get("options") or {}, text)


def check_options(path: Path, options: dict, text: str) -> None:
    """Every declared choice has exactly one block, and every block is declared."""
    blocks = OPTION_BLOCK.findall(text)
    if len(OPTION_MARKER.findall(text)) != 2 * len(blocks):
        error(path, "unbalanced or malformed `<!-- optie x=y -->` / `<!-- /optie -->` markers")
    found: dict[str, list[str]] = {}
    for opt, choice, _ in blocks:
        found.setdefault(opt, []).append(choice)
    for opt, spec in options.items():
        choices = set((spec or {}).get("keuzes") or {})
        if not spec.get("vraag"):
            error(path, f"option `{opt}` needs a `vraag`")
        if spec.get("default") not in choices:
            error(path, f"option `{opt}`: default must be one of {sorted(choices)}")
        got = found.get(opt, [])
        if sorted(got) != sorted(choices):
            error(path, f"option `{opt}`: blocks {sorted(got)} do not match keuzes {sorted(choices)}")
    for opt in sorted(set(found) - set(options)):
        error(path, f"option block `{opt}` not declared in `options`")


def check_skill(path: Path) -> None:
    try:
        meta = load_frontmatter(path)
    except ValueError as exc:
        error(path, str(exc))
        return
    if meta.get("name") != path.parent.name:
        error(path, f"`name` must equal folder name `{path.parent.name}`")
    if not meta.get("description"):
        error(path, "missing `description`")


def check_marketplace() -> None:
    path = ROOT / ".claude-plugin" / "marketplace.json"
    market = json.loads(path.read_text(encoding="utf-8"))
    for plugin in market.get("plugins", []):
        src = ROOT / plugin["source"]
        manifest = src / ".claude-plugin" / "plugin.json"
        if not manifest.is_file():
            error(path, f"plugin `{plugin['name']}`: {manifest.relative_to(ROOT)} missing")
            continue
        if json.loads(manifest.read_text(encoding="utf-8")).get("name") != plugin["name"]:
            error(manifest, "name differs from marketplace entry")
        mcp = src / ".mcp.json"
        if mcp.is_file():
            json.loads(mcp.read_text(encoding="utf-8"))


ALLOWED_LICENSES = {"MIT", "CC-BY-4.0"}
ALLOWED_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".toml", ".py", ".txt", ""}
# Launch visuals for the README only, see DECISIONS.md principle 2.
MEDIA_DIR = "assets"
MEDIA_SUFFIXES = {".jpg", ".png", ".mp4"}
SPDX = re.compile(r"SPDX-License-Identifier\s*=?\s*:?\s*\"?([A-Za-z0-9.+-]+)")


def check_repo_files() -> None:
    """Markdown-first and only MIT / CC BY 4.0, see DECISIONS.md principles 2 and 3."""
    licenses = {p.stem for p in (ROOT / "LICENSES").iterdir()}
    for name in sorted(licenses - ALLOWED_LICENSES):
        error(ROOT / "LICENSES", f"license `{name}` not allowed; only {sorted(ALLOWED_LICENSES)}")
    tracked = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout.split()
    for path in sorted(ROOT / f for f in tracked):
        rel = path.relative_to(ROOT)
        if not path.is_file() or rel.parts[0] == "LICENSES":
            continue
        if rel.parts[0] == MEDIA_DIR and path.suffix.lower() in MEDIA_SUFFIXES:
            continue
        if path.suffix.lower() not in ALLOWED_SUFFIXES:
            error(path, f"file type `{path.suffix}` not allowed; Markdown and plain text only")
            continue
        if path.parent.name != "templates" and "templates" in rel.parts and path.suffix != ".md":
            error(path, "templates must be Markdown")
        if path == Path(__file__).resolve():
            continue
        for found in SPDX.findall(path.read_text(encoding="utf-8", errors="ignore")):
            if found not in ALLOWED_LICENSES:
                error(path, f"license `{found}` not allowed; only {sorted(ALLOWED_LICENSES)}")


def main() -> int:
    check_repo_files()
    for path in template_files():
        check_template(path)
    for path in sorted(ROOT.glob("plugins/*/skills/*/SKILL.md")):
        check_skill(path)
    check_marketplace()
    for line in errors:
        print(f"::error::{line}")
    print(f"{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
