#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${REPO_ROOT}/.venv"

if [ ! -d "${VENV_DIR}" ]; then
  python3 -m venv "${VENV_DIR}"
fi

source "${VENV_DIR}/bin/activate"

python -m pip install --upgrade pip setuptools wheel
python -m pip install -r "${REPO_ROOT}/.devcontainer/requirements.txt"

python - <<'PY'
import csp

print(f"Installed csp {csp.__version__}")
PY

if command -v codex >/dev/null 2>&1; then
  codex --version
else
  echo "codex is not installed" >&2
  exit 1
fi
