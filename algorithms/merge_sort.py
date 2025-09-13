"""
Merge sort algorithm.

Merge sort is a divide-and-conquer algorithm that splits the input list into
halves, recursively sorts each half, and then merges the sorted halves.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""
from typing import List, Any

def merge_sort(data: List[Any]) -> List[Any]:
    """Return a new list containing all items from *data* in sorted order."""
    if len(data) <= 1:
        return data[:]
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return _merge(left, right)

def _merge(left: List[Any], right: List[Any]) -> List[Any]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
