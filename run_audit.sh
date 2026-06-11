#!/usr/bin/env bash
# run_audit.sh  Bash driver for the server disk-usage audit.
# Discovers a Python interpreter, runs check_usage.py, and
# saves timestamped output to reports/.

set -euo pipefail

#  Configuration 
DATA="data/server_usage.txt"
REPORTS_DIR="reports"
TIMESTAMP="$(date +"%Y%m%d_%H%M%S")"
REPORT="${REPORTS_DIR}/disk_report_${TIMESTAMP}.txt"
LATEST="${REPORTS_DIR}/disk_report_latest.txt"
PYTHON_CMD=""
MAX_REPORTS=10   # keep only the 10 most recent reports

#  Banner 
echo "================================================"
echo "  Server Disk Usage Audit"
echo "  Timestamp: $(date -u +"%Y-%m-%d %H:%M:%SZ")"
echo "================================================"

#  Find a usable Python interpreter 
for cmd in python3 python py python2; do
  if command -v "$cmd" >/dev/null 2>&1; then
      PYTHON_CMD="$cmd"
          break
            fi
            done

            if [ -z "$PYTHON_CMD" ]; then
              echo "ERROR: No Python interpreter found in PATH." >&2
                echo "Install Python 3 and try again."             >&2
                  exit 1
                  fi

                  echo "Using interpreter: $PYTHON_CMD ($($PYTHON_CMD --version 2>&1))"

                  #  Ensure data file exists 
                  if [ ! -f "$DATA" ]; then
                    echo "ERROR: Data file not found: $DATA" >&2
                      exit 1
                      fi

                      #  Ensure reports directory exists 
                      mkdir -p "$REPORTS_DIR"

                      #  Run audit and capture output 
                      echo ""
                      echo "Running audit..."
                      if "$PYTHON_CMD" scripts/check_usage.py --file "$DATA" | tee "$REPORT"; then
                        # Also update the 'latest' symlink-style copy for easy access
                          cp "$REPORT" "$LATEST"
                            echo ""
                              echo "Audit complete."
                                echo "  Timestamped report : $REPORT"
                                  echo "  Latest report copy : $LATEST"
                                  else
                                    echo "ERROR: Audit script exited with errors." >&2
                                      exit 2
                                      fi

                                      #  Rotate old reports (keep MAX_REPORTS most recent) 
                                      REPORT_COUNT=$(find "$REPORTS_DIR" -maxdepth 1 -name 'disk_report_[0-9]*.txt' | wc -l)
                                      if [ "$REPORT_COUNT" -gt "$MAX_REPORTS" ]; then
                                        find "$REPORTS_DIR" -maxdepth 1 -name 'disk_report_[0-9]*.txt' \
                                            | sort \
                                                | head -n $(( REPORT_COUNT - MAX_REPORTS )) \
                                                    | xargs rm -f
                                                      echo "Rotated old reports (kept last ${MAX_REPORTS})."
                                                      fi

                                                      exit 0
                                                      
