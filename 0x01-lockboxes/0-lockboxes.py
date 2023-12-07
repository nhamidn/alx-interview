#!/usr/bin/python3
"""Lockboxes module."""


def dfs(boxes, idx, visited):
    """Function that implement the dfs algorithm."""
    for key in boxes[idx]:
        if not visited[key]:
            visited[key] = True
            dfs(boxes, key, visited)


def canUnlockAll(boxes):
    """Function that check if all boxes can be opened."""
    n = len(boxes)
    if n <= 1:
        return True
    visited = [False] * n
    visited[0] = True

    dfs(boxes, 0, visited)

    return all(visited)
