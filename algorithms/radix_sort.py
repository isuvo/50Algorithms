"""Radix sort algorithm for non-negative integers (base 10, LSD variant).

Sorts numbers digit by digit using counting sort as a subroutine.
Time Complexity: O(d * (n + b)) where d is number of digits and b is base.
Space Complexity: O(n + b)
"""

def radix_sort(arr):
    """Return a new list containing the sorted elements of *arr* using radix sort."""
    if not arr:
        return []
    result = arr[:]
    max_val = max(result)
    exp = 1
    while max_val // exp > 0:
        count = [0] * 10
        output = [0] * len(result)
        for num in result:
            index = (num // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for num in reversed(result):
            index = (num // exp) % 10
            count[index] -= 1
            output[count[index]] = num
        result = output
        exp *= 10
    return result
