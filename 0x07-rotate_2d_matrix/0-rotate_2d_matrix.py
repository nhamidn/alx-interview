#!/usr/bin/python3
"""
Rotate 2d matrix module.
"""


def rotate_2d_matrix(matrix):
    """Function that rotate 2d matrix by 90 degrees clockwise."""
    l_line = len(matrix[0])
    l = l_line**2
    m_test = [[-1, -1, -1],
              [-1, -1, -1],
              [-1, -1, -1]]
    n = int((l) / 2)
    for i in range(l):
        x = int(i / l_line)
        y = int(i % l_line)
        m_test[y][l_line-x-1] = matrix[x][y]
        #m_test[x][y] = matrix[l_line-y-1][x]

    for row in m_test:
        print(row)

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    #print(matrix)
