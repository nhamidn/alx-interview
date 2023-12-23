#!/usr/bin/python3
"""
0-minioperations Module.
"""
import math


def minOperations(n):
    """Method that calculates the fewest number of operations."""
    if n <= 0:
        return 0
    l2 = int(math.log2(n) * 2)
    half = int(n / 2)
    num = n
    num_op = 0
    while half:
        if num % half == 0:
            num_op += 1
            num_op += (int(num / half) - 1)
            num = half
            half = int(half / 2)
        else:
            half -= 1
    result = l2 if (l2 < num_op and pow(1, l2) == n) else num_op
    return result
