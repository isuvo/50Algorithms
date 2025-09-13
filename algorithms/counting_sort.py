"""Counting sort algorithm for non-negative integers.

Counts the occurrences of each value and reconstructs the sorted list.
Time Complexity: O(n + k) where k is the range of the input.
Space Complexity: O(k)
"""

def counting_sort(arr, max_val=None):
    """Return a new list containing the sorted elements of *arr* using counting sort."""
    if not arr:
        return []
    if max_val is None:
        max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    output = []
    for num, c in enumerate(count):
        output.extend([num] * c)
    return output
