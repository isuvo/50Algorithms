"""Insertion sort algorithm.

This in-place, comparison-based algorithm builds the sorted array one item at a time
by inserting each element into its correct position within the already sorted portion.
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def insertion_sort(arr):
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
