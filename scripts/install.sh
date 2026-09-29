#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/skills/combover"
TARGET="${1:-all}"

copy_skill() {
  local dest="$1"
  mkdir -p "$(dirname "$dest")"
  rm -rf "$dest"
  cp -R "$SRC" "$dest"
  printf 'installed: %s
' "$dest"
}

case "$TARGET" in
  all)
    copy_skill "$HOME/.agents/skills/combover"
    copy_skill "$HOME/.claude/skills/combover"
    copy_skill "$HOME/.cursor/skills/combover"
    copy_skill "$HOME/.gemini/skills/combover"
    copy_skill "$HOME/.config/opencode/skills/combover"
    ;;
  agents)   copy_skill "$HOME/.agents/skills/combover" ;;
  claude)   copy_skill "$HOME/.claude/skills/combover" ;;
  cursor)   copy_skill "$HOME/.cursor/skills/combover" ;;
  gemini)   copy_skill "$HOME/.gemini/skills/combover" ;;
  opencode) copy_skill "$HOME/.config/opencode/skills/combover" ;;
  *)
    echo "usage: $0 [all|agents|claude|cursor|gemini|opencode]" >&2
    exit 2
    ;;
esac
