"""Quickselect algorithm to find the k-th smallest element.

Uses the same partitioning idea as quicksort but only recurses into one partition.
Time Complexity: O(n) average, O(n^2) worst, where n is the number of elements.
Space Complexity: O(log n) average for recursion stack, where n is the number of elements.
"""

import random
from typing import List, TypeVar

T = TypeVar("T")

def quickselect(arr: List[T], k: int) -> T:
    """Return the k-th smallest element of *arr* (0-indexed) using quickselect."""
    if not 0 <= k < len(arr):
        raise ValueError("k must be a valid index in the list")
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

if __name__ == "__main__":
    my_list = [3, 7, 2, 1, 9, 5, 4, 6, 8]
    kth_smallest = quickselect(my_list, 4) # 5th smallest element
    print(f"The 5th smallest element is: {kth_smallest}")