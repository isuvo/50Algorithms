"""Bucket sort algorithm for numbers in [0, 1).

Distributes input numbers into a fixed number of buckets, sorts each bucket, and
concatenates the results.
Time Complexity: O(n + k) average
Space Complexity: O(n)
"""

def bucket_sort(arr, bucket_count=10):
    """Return a new list containing the sorted elements of *arr* using bucket sort."""
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = min(bucket_count - 1, int(num * bucket_count))
        buckets[index].append(num)
    for bucket in buckets:
        bucket.sort()
    return [num for bucket in buckets for num in bucket]
