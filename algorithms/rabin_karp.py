"""Rabin-Karp substring search algorithm using rolling hash.

Computes hash values to quickly skip non-matching segments.
Time Complexity: O(n + m) average
Space Complexity: O(1)
"""

def rabin_karp(text, pattern, base=256, mod=101):
    """Return starting indices where *pattern* occurs in *text* using Rabin-Karp."""
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
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
