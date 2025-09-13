"""Quickselect algorithm to find the k-th smallest element.

Uses the same partitioning idea as quicksort but only recurses into one partition.
Time Complexity: O(n) average, O(n^2) worst
Space Complexity: O(1) average (ignoring recursion stack)
"""

import random

def quickselect(arr, k):
    """Return the k-th smallest element of *arr* (0-indexed) using quickselect."""
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return quickselect(highs, k - len(lows) - len(pivots))
