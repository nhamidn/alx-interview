#!/usr/bin/python3
"""
pascal_triangle module.
"""


def pascal_triangle(n):
    """Function that prints the pascal triangle."""
    if n <= 0:
        return []
    lst = []
    for i in range(n):
        if i > 1:
            half = i + 1
            half = half if (half % 2 == 0) else (half + 1)
            half = int(half / 2)
            child = []
            for j in range(half):
                child.append(1 if j == 0 else lst[-1][j] + lst[-1][j-1])
            if (i + 1) % 2 == 0:
                child = child + child[::-1]
            else:
                child = child + child[:-1][::-1]
            lst.append(child)
        else:
            lst.append([1 for j in range(i + 1)])
    return lst
