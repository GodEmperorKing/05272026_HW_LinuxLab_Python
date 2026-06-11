# Linux Python Lab  Disk Usage Audit Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) ![Bash](https://img.shields.io/badge/Bash-Script-green?logo=gnubash) ![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey?logo=linux)

A cross-script disk-usage auditing workflow built for a Linux lab environment. A Bash driver script invokes a Python collector to gather CPU, memory, disk, and process metrics, writes a timestamped report, and archives it automatically.

---

##  Project Structure

```
05272026_HW_LinuxLab_Python/
 check_usage.py          # Python: collects system metrics
  run_audit.sh            # Bash: orchestrates the full audit
   audit_report.txt        # Latest generated report
    data/                   # Raw data inputs
     reports/                # Archived timestamped reports
      scripts/                # Additional helper scripts
       deliverables/
            screenshots/        # All lab screenshots
                    script_run.png
                            audit_report_output.png
                                    python_scripts_run.png
                                            reports_archive.png
                                                 README.md
                                                 ```

                                                 ---

                                                 ##  How to Run

                                                 ```bash
                                                 ./run_audit.sh
                                                 ```

                                                 This will:
                                                 1. Run `check_usage.py` to collect CPU, memory, disk, and process metrics
                                                 2. Write results to `audit_report.txt`
                                                 3. Save a timestamped copy to `reports/`

                                                 > **Note:** Make sure the script is executable: `chmod +x run_audit.sh`

                                                 ---

                                                 ##  Python Script  `check_usage.py`

                                                 Collects and formats system metrics using the `psutil` library:

                                                 | Metric | Description |
                                                 |--------|-------------|
                                                 | CPU Usage | Current CPU utilization (%) |
                                                 | Memory | Total, used, and free RAM |
                                                 | Disk | Usage per mounted partition |
                                                 | Processes | Top running processes by CPU |

                                                 ---

                                                 ##  Files

                                                 | File | Description |
                                                 |------|-------------|
                                                 | `check_usage.py` | Python metric collector |
                                                 | `run_audit.sh` | Bash automation driver |
                                                 | `audit_report.txt` | Most recent audit output |
                                                 | `reports/` | Archive of all past reports |
                                                 | `data/` | Lab input data |
                                                 | `scripts/` | Additional helper scripts |
                                                 | `deliverables/screenshots/` | Lab evidence screenshots |

                                                 ---

                                                 ##  Screenshots

                                                 ### Script Execution
                                                 ![Script Run](deliverables/screenshots/script_run.png
                                                 ### Python Scripts Running
                                                 ![Python Scripts Run](deliverables/screenshots/python_scripts_run.png
                                                 ### Audit Report Output
                                                 ![Audit Report Output](deliverables/screenshots/audit_report_output.png
                                                 ### Reports Archive
                                                 ![Reports Archive](deliverables/screenshots/reports_archive.png
                                                 ---

                                                 ##  Requirements

                                                 - Python 3.x
                                                 - `psutil` library  `pip install psutil`
                                                 - Bash (Linux/macOS)

                                                 ---

                                                 ##  Learning Objectives

                                                 - File I/O in Python
                                                 - Bash scripting and automation
                                                 - Error handling across scripts
                                                 - Cross-script integration (Bash  Python)
                                                 - Enhancing existing code with custom improvements

                                                 ---

                                                 *Lab completed: May 27, 2026  GodEmperorKing*