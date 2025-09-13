"""Counting sort algorithm for non-negative integers.

Counts the occurrences of each value and reconstructs the sorted list.
Time Complexity: O(n + k) where n is the number of elements and k is the range
of the input.
Space Complexity: O(k) where k is the range of the input.
"""
from typing import List, Optional

def counting_sort(arr: List[int], max_val: Optional[int] = None) -> List[int]:
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

if __name__ == "__main__":
    unsorted_list = [4, 2, 2, 8, 3, 3, 1]
    sorted_list = counting_sort(unsorted_list)
    print(f"Unsorted list: {unsorted_list}")
    print(f"Sorted list: {sorted_list}")