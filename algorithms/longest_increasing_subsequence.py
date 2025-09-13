"""
Longest Increasing Subsequence (LIS).

This implementation of the LIS algorithm finds the longest subsequence of a
given sequence in which the subsequence's elements are in sorted order, lowest
to highest, and in which the subsequence is as long as possible. This
subsequence is not necessarily contiguous or unique.

Time Complexity: O(n log n), where n is the length of the sequence.
Space Complexity: O(n), where n is the length of the sequence.
"""
from bisect import bisect_left
from typing import List, TypeVar

T = TypeVar("T")

def lis(seq: List[T]) -> List[T]:
    """
    Return one longest increasing subsequence of seq.

    Args:
        seq: The input sequence.

    Returns:
        A longest increasing subsequence of the input sequence.
    """
    if not seq:
        return []
    piles = []
    pile_tops = []
    parent = [-1] * len(seq)
    for i, x in enumerate(seq):
        j = bisect_left(piles, x)
        if j == len(piles):
            piles.append(x)
            pile_tops.append(i)
        else:
            piles[j] = x
            pile_tops[j] = i
        if j > 0:
            parent[i] = pile_tops[j - 1]
    k = pile_tops[-1]
    res = []
    while k != -1:
        res.append(seq[k])
        k = parent[k]
    return res[::-1]

if __name__ == "__main__":
    sequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    longest_subsequence = lis(sequence)
    print(f"The longest increasing subsequence is: {longest_subsequence}")