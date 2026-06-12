🐧 Linux Lab – Python Disk Usage Audit
This project implements a simple automated disk‑usage audit workflow using a Bash script and a Python script.
The goal of the lab is to practice Linux scripting, Python file parsing, and cross‑script integration while generating a clean, timestamped disk‑usage report.

📂 Project Overview
The workflow consists of:

run_audit.sh  
A Bash automation script that:

Logs a timestamp

Detects a working Python interpreter

Validates required files

Executes the Python script

Reports success or failure

scripts/check_usage.py  
A Python script that:

Reads server usage data

Sorts usage values

Flags high‑usage servers

Calculates averages

Generates a formatted report

data/server_usage.txt  
The input data file containing disk‑usage values.

reports/disk_report.txt  
The generated output report.

deliverables/  
Contains screenshots and documentation proving successful execution.

▶️ How to Run the Audit
From the project root: ./run_audit.sh
This will:

Validate the environment

Run the Python script

Generate a timestamped report

Save it to reports/disk_report.txt

To view the report: cat reports/disk_report.txt

🧠 What I Learned
Working through this lab reinforced several key concepts:

✔ Linux scripting fundamentals
Creating a Bash script that validates the environment and executes another script.

✔ Python file parsing
Reading structured text, splitting values, sorting, and generating formatted output.

✔ Cross‑script integration
Using Bash to orchestrate Python execution and manage file paths.

✔ Error handling
Ensuring the workflow fails cleanly when files or interpreters are missing.

⚠️ Challenges Encountered
1. Parsing whitespace‑based data
The original usage file required careful splitting and trimming to ensure Python parsed each line correctly.

2. Interpreter inconsistencies
Different systems use python, python3, or py.
The Bash script was updated to detect a working interpreter automatically.

3. Directory structure issues
Ensuring the reports/ directory existed before writing the output file.

📸 Deliverables
All screenshots demonstrating the working audit process are located in: deliverables/screenshots/
These include:

Running the Bash script

Viewing the generated report

Running the Python script directly

Listing the reports directory

Viewing the report file



