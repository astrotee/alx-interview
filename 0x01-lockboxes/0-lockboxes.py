#!/usr/bin/python3
""""lockboxes"""


def canUnlockAll(boxes: list):
    "check if all boxes are reachable"
    if len(boxes) == 0:
        return True
    unvisited = set(range(1, len(boxes)))
    dfs(boxes[0], boxes, unvisited)
    return len(unvisited) == 0


def dfs(box: list, boxes: list, unvisited: set):
    "do a dfs on boxes"
    for key in box:
        if key in unvisited and key in range(1, len(boxes)):
            unvisited.remove(key)
            dfs(boxes[key], boxes, unvisited)
