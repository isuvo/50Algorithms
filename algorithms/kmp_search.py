"""Knuth-Morris-Pratt substring search algorithm.

Uses a prefix table to avoid redundant comparisons.
Time Complexity: O(n + m)
Space Complexity: O(m)
"""

def kmp_search(text, pattern):
    """Return starting indices where *pattern* is found within *text*."""
    if pattern == "":
        return list(range(len(text) + 1))
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    res = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                res.append(i - j + 1)
                j = lps[j - 1]
    return res
