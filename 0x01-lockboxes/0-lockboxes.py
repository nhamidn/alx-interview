#!/usr/bin/python3
"""Lockboxes module."""


def canUnlockAll(boxes):
    """Function that check if all boxes can be opened using dfs algorithm."""
    if (type(boxes)) is not list:
        return False
    n = len(boxes)
    if n == 0:
        return False
    visited = [False] * n
    visited[0] = True

    def dfs(boxes, idx, visited):
        """Function that implement the dfs algorithm."""
        for key in boxes[idx]:
            if key < n and not visited[key]:
                visited[key] = True
                dfs(boxes, key, visited)

    dfs(boxes, 0, visited)

    return all(visited)
