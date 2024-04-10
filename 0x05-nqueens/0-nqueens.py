#!/usr/bin/env python3
"""0-nqueens module.
"""


import sys


def solve(n: int) -> None:
    """Function that solves the problem."""
    print(n)
    solutions = []


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        num = int(sys.argv[1])
        if num < 4:
            print("N must be at least 4")
            sys.exit(1)
        solve(num)
    else:
        print("N must be a number")
        sys.exit(1)
