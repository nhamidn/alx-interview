#!/usr/bin/python3
"""Script that prints stats"""
import sys


def print_stats():
    """Function that print the collected stats."""
    print(f"File size: {total_files_size}")
    for code in sorted(codes.keys()):
        print(f"{code}: {codes[code]}")


codes = {}
count = 0
total_files_size = 0

for line in sys.stdin:
    count = count + 1
    parts = line.split()

    if len(parts) < 2:
        continue

    try:
        size = int(parts[-1])
    except ValueError:
        continue

    total_files_size += size

    try:
        status = int(parts[-2])
    except ValueError:
        continue

    if status in codes:
        codes[status] += 1
    else:
        codes[status] = 1

    if count % 10 == 0:
        print_stats()

if count % 10 != 0 or count == 0:
    print_stats()
