# Linux Python Lab – Disk Usage Audit Tool

This project implements a simple server disk-usage auditing workflow using:

- A Bash automation script (`run_audit.sh`)
- A Python processing script (`check_usage.py`)
- A generated report (`audit_report.txt`)
- Archived reports saved to the `reports/` folder

The goal of the lab was to practice:

- File I/O in Python
- Bash scripting
- Error handling
- Cross-script integration
- Enhancing existing code with custom improvements

---

## How to Run

```bash
./run_audit.sh
```

This will:
1. Run `check_usage.py` to collect CPU, memory, disk, and process metrics
2. Write the results to `audit_report.txt`
3. Save a timestamped copy to `reports/`

## Files

| File | Description |
|---|---|
| `check_usage.py` | Python script that reads `/proc` and `os.statvfs` to gather system metrics |
| `run_audit.sh` | Bash runner that executes the Python script, logs output, and archives reports |
| `audit_report.txt` | Latest generated system usage report |
| `reports/` | Folder containing timestamped archive copies of past reports |

## Requirements

- Linux (reads `/proc/stat`, `/proc/meminfo`)
- Python 3
- Bash
