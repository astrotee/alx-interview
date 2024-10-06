#!/usr/bin/python3
""""pascals triangle"""


def pascal_triangle(n):
    "generate pascal triangle of hight n"

    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]

    tri = pascal_triangle(n-1)
    new_row = [1] * n
    last_row = tri[-1]
    for i in range(1, n-1):
        new_row[i] = last_row[i-1] + last_row[i]
    tri.append(new_row)
    return tri
