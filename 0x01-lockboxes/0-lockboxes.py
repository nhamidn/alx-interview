#!/usr/bin/python3
"""Lockboxes module."""


def canUnlockAll(boxes):
    """Function that check if all boxes can be opened using bfs algorithm."""
    if (type(boxes)) is not list:
        return False
    n = len(boxes)
    if n == 0:
        return False

    queue = [0]
    unlocked_boxes = [0]
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key not in unlocked_boxes:
                unlocked_boxes.append(key)
                queue.append(key)
    return n == len(unlocked_boxes)
