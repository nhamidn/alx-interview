#!/usr/bin/python3
"""making_change module."""

import sys


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount.
    """
    if total <= 0:
        return 0
    dpv1 = {}
    dpv1[0] = 0
    for c in coins:
        if c <= total:
            for i in range(c, total + 1):
                prev = dpv1.get((i - c), sys.maxsize)
                curr = dpv1.get(i, sys.maxsize)
                if prev < sys.maxsize:
                    dpv1[i] = min(curr, 1 + prev)
    result = dpv1.get(total, -1)
    return result
