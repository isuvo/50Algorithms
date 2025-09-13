"""
Binary search algorithm.

This function searches for a target value within a sorted list by repeatedly
splitting the search interval in half. At each step it compares the target with
the middle element and continues in the half where the target may reside.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import Sequence, Any, Optional

def binary_search(data: Sequence[Any], target: Any) -> Optional[int]:
    """Return the index of *target* in the sorted sequence *data* or ``None``.

    Parameters
    ----------
    data: Sequence[Any]
        A sorted sequence to search through.
    target: Any
        The value to locate.
    """
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None
