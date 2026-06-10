#!/usr/bin/env bash

set -euo pipefail

REPORT="reports/disk_report.txt"
DATA="data/server_usage.txt"
PYTHON_CMD=""

echo "Starting server audit"
echo "Timestamp: $(date -u +"%Y-%m-%d %H:%M:%SZ")"

# Find a usable Python command
for cmd in python3 python py python; do
  if command -v "$cmd" >/dev/null 2>&1; then
    PYTHON_CMD="$cmd"
    break
  fi
done

if [ -z "$PYTHON_CMD" ]; then
  echo "ERROR: No Python interpreter found in PATH"
  exit 1
fi

# Ensure data file exists
if [ ! -f "$DATA" ]; then
  echo "ERROR: Data file not found: $DATA"
  exit 1
fi

# Ensure reports directory exists
mkdir -p "$(dirname "$REPORT")"

# Run the Python script and capture its exit code
if "$PYTHON_CMD" scripts/check_usage.py; then
  echo "Audit complete"
  echo "Report saved to $REPORT"
  exit 0
else
  echo "Audit FAILED — Python script returned an error"
  exit 2
fi
