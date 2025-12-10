#!/usr/bin/env bash
set -euo pipefail
MODE=${1:-}
if [ "$MODE" = "dynamic" ]; then
	PORT=${2:-8000}
	echo "Serving workspace with dynamic index at http://localhost:${PORT}"
	python3 serve_dynamic.py "$PORT"
else
	PORT=${1:-8000}
	echo "Serving 'apps' at http://localhost:${PORT}"
	python3 -m http.server "$PORT" --directory apps
fi
