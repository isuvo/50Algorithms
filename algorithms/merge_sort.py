"""
Merge sort algorithm.

Merge sort is a divide-and-conquer algorithm that splits the input list into
halves, recursively sorts each half, and then merges the sorted halves.

Time Complexity: O(n log n), where n is the number of elements.
Space Complexity: O(n), where n is the number of elements.
"""
from typing import List, Any, TypeVar

T = TypeVar("T")

def merge_sort(data: List[T]) -> List[T]:
    """Return a new list containing all items from *data* in sorted order."""
    if len(data) <= 1:
        return data[:]
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return _merge(left, right)

def _merge(left: List[T], right: List[T]) -> List[T]:
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

if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = merge_sort(unsorted_list)
    print(f"Unsorted list: {unsorted_list}")
    print(f"Sorted list: {sorted_list}")