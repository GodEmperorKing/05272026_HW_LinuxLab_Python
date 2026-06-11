#!/usr/bin/env python3
"""check_usage.py

Reads a CSV file of server disk-usage records and prints a
WARNING / OK status for each server based on a configurable
threshold.  Designed to be called by run_audit.sh.

Usage:
    python3 scripts/check_usage.py
        python3 scripts/check_usage.py --file data/server_usage.txt
            python3 scripts/check_usage.py --file data/server_usage.txt --threshold 90

            CSV format (no header):
                >server_name>,>disk_usage_percent>
                    Example:  web-01,75
                    """

import argparse
import sys


DEFAULT_FILE = "data/server_usage.txt"
DEFAULT_THRESHOLD = 80


def parse_args():
        parser = argparse.ArgumentParser(
                    description="Check server disk usage from a CSV data file."
        )
        parser.add_argument(
            "--file",
            default=DEFAULT_FILE,
            help=f"Path to the CSV data file (default: {DEFAULT_FILE})",
        )
        parser.add_argument(
            "--threshold",
            type=int,
            default=DEFAULT_THRESHOLD,
            help=f"Warning threshold in percent (default: {DEFAULT_THRESHOLD})",
        )
        return parser.parse_args()


def check_usage(file_path, threshold):
        """Read the data file and print a status line for each server."""
        print("SERVER DISK USAGE REPORT")
        print("=" * 40)

    try:
                with open(file_path, "r") as file:
                                for line_num, line in enumerate(file, start=1):
                                                    line = line.strip()
                                                    if not line:          # skip blank lines
                                                        continue

                parts = line.split(",")
                        if len(parts) != 2:
                                                print(
                                                                            f"  [SKIP] Line {line_num}: unexpected format -> {line!r}",
                                                                            file=sys.stderr,
                                                )
                                                continue

                server_name, usage_str = parts
                server_name = server_name.strip()
                usage_str = usage_str.strip()

                try:
                                        usage = int(usage_str)
except ValueError:
                    print(
                                                f"  [SKIP] Line {line_num}: non-integer usage value "
                                                f"-> {usage_str!r}",
                                                file=sys.stderr,
                    )
                    continue

                if usage >= threshold:
                                        print(f"  WARNING: {server_name} is at {usage}% disk usage")
else:
                    print(f"  OK:      {server_name} is at {usage}% disk usage")

except FileNotFoundError:
        print(f"ERROR: Data file not found -> {file_path}", file=sys.stderr)
        sys.exit(1)
except PermissionError:
        print(f"ERROR: Permission denied reading -> {file_path}", file=sys.stderr)
        sys.exit(1)

    print("=" * 40)


if __name__ == "__main__":
        args = parse_args()
    check_usage(args.file, args.threshold)
