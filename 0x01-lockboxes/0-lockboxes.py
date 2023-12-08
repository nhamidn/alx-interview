#!/usr/bin/python3
"""Lockboxes module."""


def canUnlockAll(boxes):
    """Function that checks if all boxes can be opened."""
    n = len(boxes)
    if n == 0:
        return False
    visited = [False] * n
    visited[0] = True

    stack = [0]
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
