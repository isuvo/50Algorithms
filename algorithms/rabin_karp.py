"""Rabin-Karp substring search algorithm using rolling hash.

Computes hash values to quickly skip non-matching segments.
Time Complexity: O(n + m) average, where n is the length of the text and m is
the length of the pattern.
Worst-case Time Complexity: O(n*m).
Space Complexity: O(1).
"""
from typing import List

def rabin_karp(text: str, pattern: str, base: int = 256, mod: int = 101) -> List[int]:
    """Return starting indices where *pattern* occurs in *text* using Rabin-Karp."""
    n, m = len(text), len(pattern)
    if m == 0:
        return list(range(n + 1))
    if m > n:
        return []
    h = pow(base, m - 1, mod)
    p = t = 0
    for i in range(m):
        p = (p * base + ord(pattern[i])) % mod
        t = (t * base + ord(text[i])) % mod
    res = []
    for i in range(n - m + 1):
        if p == t and text[i : i + m] == pattern:
            res.append(i)
        if i < n - m:
            t = (t - ord(text[i]) * h) * base + ord(text[i + m])
            t %= mod
    return res

if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    indices = rabin_karp(text, pattern)
    if indices:
        print(f'Pattern "{pattern}" found at indices: {indices}')
    else:
        print(f'Pattern "{pattern}" not found')