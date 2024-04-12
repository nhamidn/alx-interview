#!/usr/bin/python3
"""0-nqueens module.
"""


import sys
from typing import List


def is_safe(x: int, y: int, solutions: List) -> bool:
    """Function that check is a position is safe"""
    for e in solutions:
        if x == e[0] or y == e[1]:
            return False
        if abs(x - e[0]) == abs(y - e[1]):
            return False
    return True


def solve(n: int, col: int, solutions: List) -> bool:
    """Function that solves the problem."""
    if col >= n:
        print(solutions)
        return True
    for i in range(n):
        if is_safe(col, i, solutions):
            solutions.append([col, i])
            solve(n, col + 1, solutions)
            solutions.pop(col)
    return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
        if num < 4:
            print("N must be at least 4")
            sys.exit(1)
        for i in range(num):
            solutions = []
            solutions.append([0, i])
            solve(num, 1, solutions)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
