"""Knuth-Morris-Pratt substring search algorithm.

Uses a prefix table to avoid redundant comparisons.
Time Complexity: O(n + m), where n is the length of the text and m is the length
of the pattern.
Space Complexity: O(m), where m is the length of the pattern.
"""
from typing import List

def kmp_search(text: str, pattern: str) -> List[int]:
    """Return starting indices where *pattern* is found within *text*."""
    if not pattern:
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

if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    indices = kmp_search(text, pattern)
    if indices:
        print(f'Pattern "{pattern}" found at indices: {indices}')
    else:
        print(f'Pattern "{pattern}" not found')