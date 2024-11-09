#!/usr/bin/python3
"N queens"
import sys
from typing import List


def nqueens(N: int) -> List[List[int]]:
    "solve N queens"
    global solution
    solutions = []
    solution = []
    board = [[False] * N for _ in range(N)]

    def is_valid(row: int, col: int):
        "check if move is valid"
        for i in range(row, -1, -1):
            if board[i][col]:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j]:
                return False
        for i, j in zip(range(row, -1, -1), range(col, N)):
            if board[i][j]:
                return False
        return True

    def dfs(row: int) -> bool:
        "search for solutions"
        global solution
        if row >= N:
            solutions.append(solution.copy())
            return True
        for col in range(N):
            if is_valid(row, col):
                board[row][col] = True
                solution.append([row, col])
                dfs(row + 1)
                solution.pop()
                board[row][col] = False
        return False

    dfs(0)

    return solutions


def main():
    "main Function"
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)
    for sol in nqueens(N):
        print(sol)


if __name__ == "__main__":
    main()
