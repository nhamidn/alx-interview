#!/usr/bin/python3
"""Script that prints stats"""
import sys


codes = {}
count = 0
total_files_size = 0

for line in sys.stdin:
    count = count + 1
    parts = line.split()

    if len(parts) < 2:
        continue

    try:
        status = int(parts[-2])
        size = int(parts[-1])
    except ValueError:
        continue

    total_files_size += size

    if status in codes:
        codes[status] += 1
    else:
        codes[status] = 1

    if count % 10 == 0:
        print(f"File size: {total_files_size}")
        for code in sorted(codes.keys()):
            print(f"{code}: {codes[code]}")
        pass
    pass
