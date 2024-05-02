#!/usr/bin/python3
"""making_change module."""

import sys


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount.
    """
    if total <= 0:
        return 0
    dp = [sys.maxsize] * (total + 1)
    dp[0] = 0
    for c in coins:
        if c <= total:
            for i in range(c, total + 1):
                prev = i - c
                if dp[prev] != sys.maxsize:
                    new_count = 1 + dp[prev]
                    if new_count < dp[i]:
                        dp[i] = new_count
    return dp[total] if dp[total] != sys.maxsize else -1
