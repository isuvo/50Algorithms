"""Heap sort algorithm using Python's heapq module.

Builds a heap from the input and repeatedly extracts the smallest element.
Time Complexity: O(n log n), where n is the number of elements.
Space Complexity: O(n) for the heap, or O(1) if done in-place.
"""

import heapq
from typing import List, TypeVar

T = TypeVar("T")

def heap_sort(arr: List[T]) -> List[T]:
    """Return a new list containing the sorted elements of *arr* using heap sort."""
    h = arr[:]
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]

if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = heap_sort(unsorted_list)
    print(f"Unsorted list: {unsorted_list}")
    print(f"Sorted list: {sorted_list}")