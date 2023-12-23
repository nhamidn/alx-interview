#!/usr/bin/python3
"""
0-minioperations Module.
"""
import math


def minOperations(n):
    """Method that calculates the fewest number of operations."""
    l2 = int(math.log2(n) * 2)
    half = int(n / 2)
    num = n
    num_op = 0
    while half:
        if num % half == 0:
            num_op += 1
            num_op += int(num / half)
            half = int(half / 2)
            num = half
        else:
            half -= 1
    result = l2 if l2 < num_op else num_op
    return result
