#!/bin/bash

echo "Running disk usage audit..."
du -sh /home > data/disk_usage.txt
echo "Audit complete. Results saved to data/disk_usage.txt."
python3 check_usage.py
