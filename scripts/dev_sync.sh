#!/usr/bin/env bash
# Sync Examples from uv.lock (PyPI cellpy), then overlay a local editable
# cellpy checkout. Other users: just run `uv sync` — nothing path-specific is
# committed.
#
# Usage:
#   scripts/dev_sync.sh                 # default: ../cellpy
#   scripts/dev_sync.sh /path/to/cellpy
#   CELLPY_ROOT=/path/to/cellpy scripts/dev_sync.sh
#   scripts/dev_sync.sh --pypi          # drop overlay; back to locked PyPI cellpy
set -euo pipefail
cd "$(dirname "$0")/.."

if [[ "${1:-}" == "--pypi" ]]; then
  uv sync
  rm -f .envrc
  echo "Using PyPI cellpy from uv.lock (local overlay removed)."
  exit 0
fi

CELLPY="${1:-${CELLPY_ROOT:-../cellpy}}"
if [[ ! -f "${CELLPY}/pyproject.toml" ]]; then
  echo "error: expected cellpy checkout at ${CELLPY}" >&2
  echo "hint: pass a path, or set CELLPY_ROOT" >&2
  exit 1
fi

# Resolve to an absolute path so the editable install survives cwd changes.
CELLPY="$(cd "${CELLPY}" && pwd)"

uv sync
uv pip install -e "${CELLPY}"

# uv run auto-syncs from the lock and would reinstall PyPI cellpy. Keep the
# overlay sticky for this shell / direnv users (file is gitignored).
cat > .envrc <<'EOF'
# Local only (gitignored). Written by scripts/dev_sync.sh
export UV_NO_SYNC=1
EOF

echo "Dev env ready: cellpy editable from ${CELLPY}"
echo
echo "Keep the overlay while working:"
echo "  - export UV_NO_SYNC=1   (or: direnv allow, if you use direnv + .envrc)"
echo "  - or use .venv directly:  source .venv/bin/activate"
echo "  - or:  uv run --no-sync ..."
echo
echo "Re-run this script after a plain \`uv sync\` / \`uv add\`."
echo "Back to PyPI:  scripts/dev_sync.sh --pypi"
