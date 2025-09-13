from bisect import bisect_left

def lis(seq):
    """Return one longest increasing subsequence of seq.

    Time: O(n log n), Space: O(n)
    """
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
