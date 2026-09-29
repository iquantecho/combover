#!/usr/bin/env python3
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.2.0"
required = [
    "plugin.json",
    ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".agents/plugins/marketplace.json",
    ".github/plugin/plugin.json",
    ".github/plugin/marketplace.json",
    ".cursor-plugin/plugin.json",
    "gemini-extension.json",
    "skills/combover/SKILL.md",
    "skills/combover/references/research.md",
    "skills/combover/references/finance.md",
    "skills/combover/references/review.md",
    "skills/combover/references/cleanup.md",
    "README.md",
    "LICENSE",
    "THIRD_PARTY_NOTICES.md",
    "assets/combover.svg",
    ".github/workflows/validate.yml",
    ".github/workflows/release.yml",
]

errors = []
for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"missing {rel}")

json_files = [
    "plugin.json",
    ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".agents/plugins/marketplace.json",
    ".github/plugin/plugin.json",
    ".github/plugin/marketplace.json",
    ".cursor-plugin/plugin.json",
    "gemini-extension.json",
]
for rel in json_files:
    try:
        data = json.loads((ROOT / rel).read_text())
    except Exception as exc:
        errors.append(f"invalid json {rel}: {exc}")
        continue
    if rel.endswith("plugin.json") or rel == "gemini-extension.json":
        if data.get("name") != "combover":
            errors.append(f"wrong plugin name in {rel}")
        if data.get("version") and data.get("version") != VERSION:
            errors.append(f"version mismatch in {rel}: {data.get('version')}")

skill = (ROOT / "skills/combover/SKILL.md").read_text()
if not skill.startswith("---\n"):
    errors.append("SKILL.md must start with YAML frontmatter")
parts = skill.split("---", 2)
front = parts[1] if len(parts) >= 3 else ""
name = re.search(r"^name:\s*([^\n]+)$", front, re.M)
desc = re.search(r"^description:\s*(.+)$", front, re.M)
if not name or name.group(1).strip() != "combover":
    errors.append("SKILL.md name must be combover")
if not desc:
    errors.append("SKILL.md needs description")

for ref in ["research.md", "finance.md", "review.md", "cleanup.md"]:
    token = f"references/{ref}"
    if token not in skill:
        errors.append(f"SKILL.md does not route to {token}")
    if not (ROOT / "skills/combover/references" / ref).is_file():
        errors.append(f"missing routed reference {token}")

readme = (ROOT / "README.md").read_text()
for needle in ["Ponytail", "Dietrich Gebert", "Less overhead. Same coverage."]:
    if needle not in readme:
        errors.append(f"README missing {needle!r}")

if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print(f"OK: {len(required)} required files, manifests parse, skill routes resolve, version {VERSION}")
