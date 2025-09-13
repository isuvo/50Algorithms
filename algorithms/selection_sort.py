"""Selection sort algorithm.

The algorithm repeatedly selects the smallest remaining element and swaps it into its
correct position.
Time Complexity: O(n^2), where n is the number of elements.
Space Complexity: O(1)
"""
from typing import List, TypeVar

T = TypeVar("T")

def selection_sort(arr: List[T]) -> List[T]:
    """Return a new list containing the sorted elements of *arr* using selection sort."""
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

if __name__ == "__main__":
    unsorted_list = [64, 25, 12, 22, 11]
    sorted_list = selection_sort(unsorted_list)
    print(f"Unsorted list: {unsorted_list}")
    print(f"Sorted list: {sorted_list}")