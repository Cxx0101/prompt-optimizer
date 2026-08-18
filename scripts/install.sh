#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="prompt-optimizer"
SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

usage() {
  cat <<'USAGE'
Usage:
  ./scripts/install.sh claude [PROJECT_DIR]
  ./scripts/install.sh codex-project [PROJECT_DIR]
  ./scripts/install.sh codex-user
  ./scripts/install.sh hermes

Targets:
  Claude Code project: <project>/.claude/skills/prompt-optimizer
  Codex project:       <project>/.agents/skills/prompt-optimizer
  Codex user:          ~/.agents/skills/prompt-optimizer
  Hermes user:         ~/.hermes/skills/creative/prompt-optimizer

The installer refuses to overwrite an existing skill directory.
USAGE
}

copy_skill() {
  local target="$1"
  if [[ -e "$target" ]]; then
    echo "Refusing to overwrite existing path: $target" >&2
    exit 2
  fi

  mkdir -p "$target"
  cp "$SRC_DIR/SKILL.md" "$target/SKILL.md"
  cp -R "$SRC_DIR/agents" "$target/agents"
  cp -R "$SRC_DIR/references" "$target/references"

  echo "Installed to: $target"
}

cmd="${1:-}"
case "$cmd" in
  claude)
    project="${2:-$PWD}"
    copy_skill "$project/.claude/skills/$SKILL_NAME"
    ;;
  codex-project)
    project="${2:-$PWD}"
    copy_skill "$project/.agents/skills/$SKILL_NAME"
    ;;
  codex-user)
    copy_skill "$HOME/.agents/skills/$SKILL_NAME"
    ;;
  hermes)
    copy_skill "$HOME/.hermes/skills/creative/$SKILL_NAME"
    ;;
  *)
    usage
    exit 1
    ;;
esac
