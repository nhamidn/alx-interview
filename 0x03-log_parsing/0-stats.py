#!/usr/bin/python3
"""Script that prints stats"""
import sys


count = 0
for line in sys.stdin:
    count = count + 1
    if count == 10:
        #print stats
        print("File size: {}")
        pass
    pass
