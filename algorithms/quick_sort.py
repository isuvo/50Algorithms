"""
Quick sort algorithm.

Quick sort selects a pivot element and partitions the remaining elements into
those less than the pivot and those greater. It recursively sorts the
partitions and concatenates the results.

Average Time Complexity: O(n log n)
Worst-case Time Complexity: O(n^2)
Space Complexity: O(log n) for recursion
"""
from typing import List, Any

def quick_sort(data: List[Any]) -> List[Any]:
    if len(data) <= 1:
        return data[:]
    pivot = data[len(data) // 2]
    less = [x for x in data if x < pivot]
    equal = [x for x in data if x == pivot]
    greater = [x for x in data if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)
