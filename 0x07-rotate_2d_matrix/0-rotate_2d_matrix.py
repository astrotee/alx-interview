#!/usr/bin/python3
"Matrix rotation"


def rotate_2d_matrix(matrix):
    "rotate a 2d matrix by 90deg clockwise"
    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-j-1][i]
            matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
            matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
            matrix[j][n-i-1] = temp
