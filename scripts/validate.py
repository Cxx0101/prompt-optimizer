#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml

root = Path(__file__).resolve().parents[1]
skill = root / "SKILL.md"
errors = []

text = skill.read_text(encoding="utf-8")
if not text.startswith("---\n"):
    errors.append("SKILL.md must start with YAML frontmatter")
else:
    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append("SKILL.md frontmatter is not closed")
    else:
        try:
            meta = yaml.safe_load(parts[1]) or {}
        except Exception as e:
            errors.append(f"Invalid YAML frontmatter: {e}")
            meta = {}
        name = meta.get("name")
        desc = meta.get("description")
        if name != root.name:
            errors.append(f"name must match folder name: {root.name!r}, got {name!r}")
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name or ""):
            errors.append("name must use lowercase letters, numbers, and single hyphens")
        if not isinstance(desc, str) or not desc.strip():
            errors.append("description is required")
        elif len(desc) > 1024:
            errors.append(f"description is too long: {len(desc)} chars")

line_count = len(text.splitlines())
if line_count > 500:
    errors.append(f"SKILL.md should stay under 500 lines; got {line_count}")

refs = sorted(set(re.findall(r"`(references/[^`]+\.md)`", text)))
for ref in refs:
    if not (root / ref).exists():
        errors.append(f"missing referenced file: {ref}")

if errors:
    print("FAIL")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("OK")
print(f"skill: {root.name}")
print(f"SKILL.md lines: {line_count}")
print(f"references checked: {len(refs)}")
