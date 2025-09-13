"""Insertion sort algorithm.

This in-place, comparison-based algorithm builds the sorted array one item at a time
by inserting each element into its correct position within the already sorted portion.
Time Complexity: O(n^2), where n is the number of elements.
Space Complexity: O(1)
"""
from typing import List, TypeVar

T = TypeVar("T")

def insertion_sort(arr: List[T]) -> List[T]:
    """Return a new list containing the sorted elements of *arr* using insertion sort."""
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = insertion_sort(unsorted_list)
    print(f"Unsorted list: {unsorted_list}")
    print(f"Sorted list: {sorted_list}")