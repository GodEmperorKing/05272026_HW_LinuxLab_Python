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

---

## Deliverables

Screenshots proving lab completion. Upload to the [`deliverables/`](deliverables/) folder when done.

| # | File | What to Capture |
|---|---|---|
| 1 | `deliverables/01_script_run.png` | Terminal running `./run_audit.sh` successfully |
| 2 | `deliverables/02_report_output.png` | Full audit report printed to terminal screen |
| 3 | `deliverables/03_report_file.png` | `cat audit_report.txt` showing saved report contents |
| 4 | `deliverables/04_python_direct.png` | Terminal running `python3 check_usage.py` directly |
| 5 | `deliverables/05_archive_listing.png` | `ls reports/` showing timestamped archived report |
| 6 | `deliverables/06_repo_overview.png` | GitHub repo page showing all committed files |
