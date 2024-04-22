#!/usr/bin/python3
"""
Rotate 2d matrix module.
"""


def rotate_2d_matrix(matrix):
    """Function that rotate 2d matrix by 90 degrees clockwise."""
    l_line = len(matrix[0])
    len_m = l_line**2
    dp = {}
    n = int((len_m) / 2)
    for i in range(len_m):
        x = int(i / l_line)
        y = int(i % l_line)
        original_v = dp.get((x, y), None)
        dp[(y, l_line-x-1)] = matrix[y][l_line-x-1]
        if original_v is None:
            matrix[y][l_line-x-1] = matrix[x][y]
        else:
            matrix[y][l_line-x-1] = original_v
