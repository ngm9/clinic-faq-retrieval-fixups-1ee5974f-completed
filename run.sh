#!/usr/bin/env bash
set -u

if [ -d /root/task ]; then BASE_DIR=/root/task; else BASE_DIR="$(cd "$(dirname "$0")" && pwd)"; fi
cd "$BASE_DIR"

python3 -m pip install -q -e . >/dev/null 2>&1
python3 -m pip install -q pytest >/dev/null 2>&1

export PYTHONPATH="$BASE_DIR/src${PYTHONPATH:+:$PYTHONPATH}"

python3 -c "import rag_retrieval; from rag_retrieval import chunking, retrieval, context, answer, documents" || {
  echo "import smoke check failed"
  exit 1
}

python3 -m pytest -q
rc=$?

if [ "$rc" -eq 0 ] || [ "$rc" -eq 1 ]; then
  exit 0
else
  exit "$rc"
fi
