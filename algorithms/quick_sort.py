"""
Quick sort algorithm.

Quick sort selects a pivot element and partitions the remaining elements into
those less than the pivot and those greater. It recursively sorts the
partitions and concatenates the results.

Average Time Complexity: O(n log n), where n is the number of elements.
Worst-case Time Complexity: O(n^2), where n is the number of elements.
Space Complexity: O(log n) for recursion, where n is the number of elements.
"""
from typing import List, Any, TypeVar

T = TypeVar("T")

def quick_sort(data: List[T]) -> List[T]:
    if len(data) <= 1:
        return data[:]
    pivot = data[len(data) // 2]
    less = [x for x in data if x < pivot]
    equal = [x for x in data if x == pivot]
    greater = [x for x in data if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)

if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = quick_sort(unsorted_list)
    print(f"Unsorted list: {unsorted_list}")
    print(f"Sorted list: {sorted_list}")