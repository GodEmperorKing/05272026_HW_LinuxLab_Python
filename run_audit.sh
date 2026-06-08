#!/bin/bash

echo "Starting server audit..."

mkdir -p reports

python scripts/check_usage.py > reports/disk_report.txt

echo "Audit complete."
echo "Report saved to reports/disk_report.txt"
