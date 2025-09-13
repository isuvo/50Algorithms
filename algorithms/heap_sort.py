"""Heap sort algorithm using Python's heapq module.

Builds a heap from the input and repeatedly extracts the smallest element.
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

import heapq

def heap_sort(arr):
    """Return a new list containing the sorted elements of *arr* using heap sort."""
    h = arr[:]
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]
