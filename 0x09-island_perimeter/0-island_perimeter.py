#!/usr/bin/python3
"""Island Perimeter module."""


def island_perimeter(grid):
    """
    Function that solves calculate the perimetere of an island using dfs.
    """

    def dfs(grid, i, j, visited):
        """DFS Algorithm."""
        perimeter = 0
        m = len(grid)
        n = len(grid[0])
        if i < 0 or j < 0 or i > m-1 or j > n-1:
            return 1
        if visited[i][j]:
            return perimeter
        if grid[i][j] != 1:
            return 1
        visited[i][j] = True
        perimeter += dfs(grid, i-1, j, visited)
        perimeter += dfs(grid, i+1, j, visited)
        perimeter += dfs(grid, i, j-1, visited)
        perimeter += dfs(grid, i, j+1, visited)
        return perimeter

    m = len(grid)
    n = len(grid[0])
    visited = [[False for i in range(n)] for j in range(m)]
    for i in range(0, m):
        for j in range(0, n):
            if grid[i][j] == 1:
                return dfs(grid, i, j, visited)
    return 0
