"""Selection sort algorithm.

The algorithm repeatedly selects the smallest remaining element and swaps it into its
correct position.
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def selection_sort(arr):
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
