"""Shell sort algorithm.

Generalization of insertion sort that allows the exchange of items far apart by
using decreasing gap sequences.
Time Complexity: Depends on the gap sequence. O(n^(3/2)) is typical for the
sequence used here (n/2, n/4, ...).
Space Complexity: O(1)
"""
from typing import List, TypeVar

T = TypeVar("T")

def shell_sort(arr: List[T]) -> List[T]:
    """Return a new list containing the sorted elements of *arr* using shell sort."""
    a = arr[:]
    gap = len(a) // 2
    while gap > 0:
        for i in range(gap, len(a)):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a

if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = shell_sort(unsorted_list)
    print(f"Unsorted list: {unsorted_list}")
    print(f"Sorted list: {sorted_list}")