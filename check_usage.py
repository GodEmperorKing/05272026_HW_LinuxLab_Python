#!/usr/bin/env python3
"""
check_usage.py
Linux System Usage Monitor
HW/Lab: 05272026_HW_LinuxLab_Python
Author: GodEmperorKing
Description: Monitors CPU, memory, and disk usage on a Linux system
             and writes a summary report to audit_report.txt
"""

import os
import sys
import datetime

def get_cpu_usage():
    """
    Read CPU stats from /proc/stat and calculate usage percentage.
    """
    try:
        with open("/proc/stat", "r") as f:
            line = f.readline()
        fields = line.split()
        total  = sum(int(x) for x in fields[1:])
        idle   = int(fields[4]) + int(fields[5])
        used   = total - idle
        pct    = round((used / total) * 100, 2) if total else 0.0
        return pct
    except Exception as e:
        return f"unavailable ({e})"


def get_memory_usage():
    """
    Parse /proc/meminfo and return total, used, free (MB) and usage %.
    """
    info = {}
    try:
        with open("/proc/meminfo", "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) >= 2:
                    key = parts[0].rstrip(":")
                    val = int(parts[1])
                    info[key] = val
        total     = info.get("MemTotal", 0)
        available = info.get("MemAvailable", 0)
        used      = total - available
        def kb_to_mb(kb):
            return round(kb / 1024, 2)
        return {
            "total_mb":  kb_to_mb(total),
            "used_mb":   kb_to_mb(used),
            "free_mb":   kb_to_mb(available),
            "usage_pct": round((used / total) * 100, 2) if total else 0.0,
        }
    except Exception as e:
        return {"error": str(e)}


def get_disk_usage(path="/"):
    """
    Use os.statvfs to retrieve disk usage for a mount point.
    """
    try:
        stat = os.statvfs(path)
        total  = stat.f_frsize * stat.f_blocks
        free   = stat.f_frsize * stat.f_bfree
        used   = total - free
        pct    = round((used / total) * 100, 2) if total else 0.0
        def b_to_gb(b):
            return round(b / (1024 ** 3), 2)
        return {
            "path":      path,
            "total_gb":  b_to_gb(total),
            "used_gb":   b_to_gb(used),
            "free_gb":   b_to_gb(free),
            "usage_pct": pct,
        }
    except Exception as e:
        return {"path": path, "error": str(e)}


def get_top_processes(n=5):
    """
    Read /proc/*/status to find top-n processes by VmRSS (resident memory).
    """
    procs = []
    try:
        for entry in os.listdir("/proc"):
            if not entry.isdigit():
                continue
            status_path = f"/proc/{entry}/status"
            try:
                info = {}
                with open(status_path, "r") as f:
                    for line in f:
                        parts = line.split(":")
                        if len(parts) == 2:
                            info[parts[0].strip()] = parts[1].strip()
                name   = info.get("Name", "unknown")
                vmrss  = info.get("VmRSS", "0 kB")
                rss_kb = int(vmrss.split()[0]) if vmrss != "0 kB" else 0
                procs.append({"pid": entry, "name": name, "vmrss_mb": round(rss_kb / 1024, 2)})
            except (PermissionError, FileNotFoundError):
                continue
    except Exception:
        pass
    procs.sort(key=lambda x: x["vmrss_mb"], reverse=True)
    return procs[:n]


def generate_report(output_file="audit_report.txt"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu   = get_cpu_usage()
    mem   = get_memory_usage()
    disk  = get_disk_usage("/")
    procs = get_top_processes(5)

    lines = [
        "=" * 60,
        "  LINUX SYSTEM USAGE AUDIT REPORT",
        f"  Generated : {timestamp}",
        f"  Host      : {os.uname().nodename}",
        f"  Kernel    : {os.uname().release}",
        "=" * 60,
        "",
        "-- CPU --",
        f"  Usage        : {cpu}%",
        "",
        "-- MEMORY --",
    ]
    if "error" in mem:
        lines.append(f"  Error: {mem['error']}")
    else:
        lines += [
            f"  Total        : {mem['total_mb']} MB",
            f"  Used         : {mem['used_mb']} MB",
            f"  Available    : {mem['free_mb']} MB",
            f"  Usage        : {mem['usage_pct']}%",
        ]
    lines += ["", "-- DISK (/) --"]
    if "error" in disk:
        lines.append(f"  Error: {disk['error']}")
    else:
        lines += [
            f"  Total        : {disk['total_gb']} GB",
            f"  Used         : {disk['used_gb']} GB",
            f"  Free         : {disk['free_gb']} GB",
            f"  Usage        : {disk['usage_pct']}%",
        ]
    lines += [
        "",
        "-- TOP 5 PROCESSES (by RSS memory) --",
        f"  {'PID':<8} {'NAME':<20} {'RSS (MB)':>10}",
        f"  {'-'*8} {'-'*20} {'-'*10}",
    ]
    for p in procs:
        lines.append(f"  {p['pid']:<8} {p['name']:<20} {p['vmrss_mb']:>10}")
    lines += ["", "=" * 60, "  END OF REPORT", "=" * 60]
    report = "\n".join(lines) + "\n"
    with open(output_file, "w") as f:
        f.write(report)
    print(report)
    print(f"[check_usage.py] Report saved to '{output_file}'")
    return report


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "audit_report.txt"
    generate_report(output_file=out)
