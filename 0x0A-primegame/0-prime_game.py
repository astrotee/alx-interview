#!/usr/bin/python3
"""Prime Game"""

primes = [True for _ in range(10000 + 1)]


def count_primes(n):
    """Count the number of primes less than n"""
    global primes
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = primes[1] = False
    return sum(primes[: n + 1])


def isWinner(x, nums):
    """Prime Game"""
    if x < 1 or not nums:
        return None
    player1 = 0
    for n in nums:
        player1 += count_primes(n) % 2
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
