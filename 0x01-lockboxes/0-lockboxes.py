#!/usr/bin/python3
""""lockboxes"""
from collections import deque


def canUnlockAll(boxes: list):
    "check if all boxes are reachable"
    if len(boxes) == 0:
        return True
    unvisited = set(range(1, len(boxes)))
    bfs(boxes[0], boxes, unvisited)
    return len(unvisited) == 0


def bfs(box: list, boxes: list, unvisited: set):
    "do a bfs on boxes"
    if len(unvisited) == 0:
        return
    q = deque([box])
    while q:
        keys = q.popleft()
        for key in keys:
            if key in unvisited and key in range(1, len(boxes)):
                unvisited.remove(key)
                q.append(boxes[key])
