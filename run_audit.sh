#!/usr/bin/env bash
# ============================================================
#  run_audit.sh
#  Linux System Audit Runner
#  HW/Lab: 05272026_HW_LinuxLab_Python
#  Author: GodEmperorKing
#  Description: Runs check_usage.py and archives the report
# ============================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="${SCRIPT_DIR}/check_usage.py"
REPORT_FILE="${SCRIPT_DIR}/audit_report.txt"
LOG_FILE="${SCRIPT_DIR}/run_audit.log"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

log() {
    local level="$1"; shift
    echo "[${TIMESTAMP}] [${level}] $*" | tee -a "${LOG_FILE}"
}

log INFO "=== Linux System Audit Starting ==="
log INFO "Working directory : ${SCRIPT_DIR}"

if ! command -v python3 &>/dev/null; then
    log ERROR "python3 not found. Please install Python 3."
    exit 1
fi
log INFO "Python version    : $(python3 --version 2>&1)"

if [[ ! -f "${PYTHON_SCRIPT}" ]]; then
    log ERROR "Script not found  : ${PYTHON_SCRIPT}"
    exit 1
fi
log INFO "Running script    : ${PYTHON_SCRIPT}"

log INFO "--- Collecting system metrics ---"
python3 "${PYTHON_SCRIPT}" "${REPORT_FILE}" 2>&1 | tee -a "${LOG_FILE}"
EXIT_CODE=${PIPESTATUS[0]}

if [[ ${EXIT_CODE} -ne 0 ]]; then
    log ERROR "check_usage.py exited with code ${EXIT_CODE}"
    exit "${EXIT_CODE}"
fi

if [[ -f "${REPORT_FILE}" ]]; then
    REPORT_SIZE=$(wc -l < "${REPORT_FILE}")
    log INFO "Report generated  : ${REPORT_FILE} (${REPORT_SIZE} lines)"
else
    log ERROR "Report file was NOT created: ${REPORT_FILE}"
    exit 1
fi

ARCHIVE_FILE="${SCRIPT_DIR}/reports/audit_report_${TIMESTAMP}.txt"
mkdir -p "${SCRIPT_DIR}/reports"
cp "${REPORT_FILE}" "${ARCHIVE_FILE}"
log INFO "Archived report   : ${ARCHIVE_FILE}"

log INFO "=== Audit Complete ==="
log INFO "Latest report : ${REPORT_FILE}"
log INFO "Archive copy  : ${ARCHIVE_FILE}"

exit 0
