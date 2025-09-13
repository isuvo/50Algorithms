"""Bubble sort algorithm.

This simple comparison sort repeatedly steps through the list, swapping adjacent
items that are out of order.
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
from typing import List, TypeVar

T = TypeVar("T")

def bubble_sort(arr: List[T]) -> List[T]:
    """Return a new list containing the sorted elements of *arr* using bubble sort."""
    a = arr[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(unsorted_list)
    print(f"Unsorted list: {unsorted_list}")
    print(f"Sorted list: {sorted_list}")