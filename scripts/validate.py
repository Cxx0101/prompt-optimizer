#!/usr/bin/env python3
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
ERRORS: list[str] = []


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        ERRORS.append("SKILL.md must start with YAML frontmatter")
        return {}

    end = text.find("\n---\n", 4)
    if end == -1:
        ERRORS.append("SKILL.md frontmatter is not closed")
        return {}

    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.fullmatch(r"([a-zA-Z0-9_-]+):\s*(.+)", line)
        if not match:
            continue
        key, value = match.groups()
        result[key] = value.strip().strip('"').strip("'")
    return result


text = SKILL.read_text(encoding="utf-8")
meta = frontmatter(text)
name = meta.get("name", "")
description = meta.get("description", "")

allowed_keys = {"name", "description", "license", "allowed-tools", "metadata"}
unexpected_keys = set(meta) - allowed_keys
if unexpected_keys:
    ERRORS.append(f"unexpected frontmatter keys: {', '.join(sorted(unexpected_keys))}")
if name != ROOT.name:
    ERRORS.append(f"name must match folder name: {ROOT.name!r}, got {name!r}")
if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
    ERRORS.append("name must use lowercase letters, numbers, and single hyphens")
if len(name) > 64:
    ERRORS.append(f"name is too long: {len(name)} chars")
if not description:
    ERRORS.append("description is required")
elif len(description) > 1024:
    ERRORS.append(f"description is too long: {len(description)} chars")
elif "<" in description or ">" in description:
    ERRORS.append("description cannot contain angle brackets")

line_count = len(text.splitlines())
if line_count > 500:
    ERRORS.append(f"SKILL.md should stay under 500 lines; got {line_count}")
if re.search(r"^\s*\[TODO:[^\n]*\]\s*$", text, re.MULTILINE):
    ERRORS.append("SKILL.md contains an unfinished TODO placeholder")

refs = sorted(set(re.findall(r"`(references/[^`]+\.md)`", text)))
for ref in refs:
    if not (ROOT / ref).is_file():
        ERRORS.append(f"missing referenced file: {ref}")

all_refs = sorted((ROOT / "references").glob("*.md"))
linked = {ROOT / ref for ref in refs}
for ref in all_refs:
    if ref not in linked:
        ERRORS.append(f"unreferenced file: {ref.relative_to(ROOT).as_posix()}")

obsolete = ("Midjourney", "FLUX", "Stable Diffusion", "Ideogram", "Nano Banana")
for path in [SKILL, *all_refs]:
    body = path.read_text(encoding="utf-8")
    for term in obsolete:
        if term in body:
            ERRORS.append(f"obsolete model {term!r} found in {path.relative_to(ROOT)}")

if ERRORS:
    print("FAIL")
    for error in ERRORS:
        print("-", error)
    sys.exit(1)

print("OK")
print(f"skill: {name}")
print(f"SKILL.md lines: {line_count}")
print(f"references checked: {len(refs)}")
