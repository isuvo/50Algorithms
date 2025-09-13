"""Bucket sort algorithm for numbers in [0, 1).

Distributes input numbers into a fixed number of buckets, sorts each bucket, and
concatenates the results.
Time Complexity: O(n + k) average, where n is the number of elements and k is
the number of buckets.
Space Complexity: O(n), where n is the number of elements.
"""
from typing import List

def bucket_sort(arr: List[float], bucket_count: int = 10) -> List[float]:
    """Return a new list containing the sorted elements of *arr* using bucket sort."""
    if not arr:
        return []
    buckets: List[List[float]] = [[] for _ in range(bucket_count)]
    for num in arr:
        index = min(bucket_count - 1, int(num * bucket_count))
        buckets[index].append(num)
    for bucket in buckets:
        # It is common to use another sorting algorithm here, like insertion sort.
        # For simplicity, we use the built-in sort().
        bucket.sort()
    return [num for bucket in buckets for num in bucket]

if __name__ == "__main__":
    unsorted_list = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    sorted_list = bucket_sort(unsorted_list)
    print(f"Unsorted list: {unsorted_list}")
    print(f"Sorted list: {sorted_list}")