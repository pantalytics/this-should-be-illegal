#!/usr/bin/env python3
"""Structural checks for templates, skills and the plugin marketplace.

Runs offline, no dependencies beyond PyYAML. Fails CI when:
- a template misses required frontmatter or cites no legal basis
- a {{placeholder}} in the body is not declared in `fields`, or vice versa
- a template marked `reviewed` has no `reviewed_by`
- `last_checked` is older than MAX_AGE_DAYS
- a skill's SKILL.md misses name/description or the name does not match its folder
- a marketplace plugin source or plugin.json is missing
"""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MAX_AGE_DAYS = 365
REQUIRED = ["title", "jurisdiction", "language", "version", "status", "last_checked", "legal_basis", "fields"]
STATUSES = {"draft", "reviewed"}
PLACEHOLDER = re.compile(r"\{\{\s*([a-z0-9_]+)\s*\}\}")

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
    declared = set((meta.get("fields") or {}).keys())
    used = set(PLACEHOLDER.findall(body(path)))
    for name in sorted(used - declared):
        error(path, f"placeholder `{{{{{name}}}}}` used but not declared in `fields`")
    for name in sorted(declared - used):
        error(path, f"field `{name}` declared but never used")


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


def main() -> int:
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
