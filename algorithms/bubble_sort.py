"""Bubble sort algorithm.

This simple comparison sort repeatedly steps through the list, swapping adjacent
items that are out of order.
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def bubble_sort(arr):
    """Return a new list containing the sorted elements of *arr* using bubble sort."""
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
