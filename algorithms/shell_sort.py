"""Shell sort algorithm.

Generalization of insertion sort that allows the exchange of items far apart by
using decreasing gap sequences.
Time Complexity: depends on gap sequence; O(n^(3/2)) typical
Space Complexity: O(1)
"""

def shell_sort(arr):
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
