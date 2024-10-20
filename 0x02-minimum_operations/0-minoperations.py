#!/usr/bin/python3
"Minimum Operations"


def minOperations(n):
    "calculates the minimum number of operations needed"
    if n <= 1:
        return 0
    factors = []
    i = 2
    while n > 1:
        if n % i:
            i += 1
        else:
            factors.append(i)
            n //= i
    return sum(factors)
