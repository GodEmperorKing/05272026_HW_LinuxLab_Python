import os

path = "data/disk_usage.txt"

with open(path, "r") as f:
    lines = f.readlines()

for line in lines:
    parts = line.strip().split()
    if len(parts) == 2:
        size = parts[0]
        directory = parts[1]
        print(f"{directory}: {size}")
