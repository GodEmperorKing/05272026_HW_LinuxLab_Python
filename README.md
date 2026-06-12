# 🐧 Linux Python Lab – Server Disk Usage Audit

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)]() 
[![Bash](https://img.shields.io/badge/shell-bash-green.svg)]() 

A modular, automated disk-usage auditing tool designed for Linux environments. This lab demonstrates cross-script orchestration, file parsing, and robust error handling.

---

## 🏗️ Project Architecture
```text
05272026_HW_LinuxLab_Python/
├── run_audit.sh           # Bash Driver (Orchestrator)
├── check_usage.py         # Python Logic (Parser)
├── server_usage.txt       # Input Data (Source of Truth)
├── audit_report.txt       # Generated Output
└── deliverables/          # Lab evidence (screenshots)

---

🛠️ Workflow Execution
1. Metadata Logging: run_audit.sh records the execution timestamp.

2. Environment Validation: Checks for the presence of input data and a functional Python interpreter.

3. Automated Auditing: Invokes check_usage.py to parse disk usage data and evaluate it against thresholds.

4. Report Generation: Saves the processed output to a structured text file for review.

---

🚀 How to Run
From the project root: chmod +x run_audit.sh
./run_audit.sh

---

🧩 Reflection (Commands + Purpose)
This lab focused on the "Bash Driver" pattern—using shell scripts to orchestrate Python logic.

echo – Tracks progress and provides console feedback during execution.

date – Stamps the audit with a clear completion time.

if [ ! -f ... ] – Logic gate to ensure the input data exists before attempting to parse it.

python3 – Invokes the Python interpreter to execute the disk usage logic.

cat – Displays the generated audit_report.txt in the terminal for immediate verification.

chmod +x – Grants the necessary execution permissions to the driver.

---

⚠️ Challenges (Refactoring & Environment)
Interpreter Inconsistencies: Different environments use python, python3, or py. The driver was designed to handle these variations to ensure reliability across systems.

Whitespace Parsing: The input file required careful string splitting and type casting (int()) to ensure the Python script correctly interpreted the usage percentages.

Modularization: I opted for a flat project structure for this lab to maintain simplicity while still separating the Bash orchestrator from the Python logic.

---

🎓 Key Takeaways
Orchestration: Using Bash to handle file paths and environment prep allows the Python logic to remain focused purely on data processing.

Data Integrity: Implementing error handling (try/except) ensures the script doesn't crash if the data file is missing or corrupted.
