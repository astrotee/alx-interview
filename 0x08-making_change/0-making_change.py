#!/usr/bin/python3
"""
Coin Change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    n = len(coins)
    count = 0
    i = 0
    while i < n and total > 0:
        if coins[i] <= total:
            total -= coins[i]
            count += 1
        else:
            i += 1
    if total != 0:
        return -1
    return count
