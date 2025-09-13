def boyer_moore(text, pattern):
    """Boyer-Moore string search using bad-character heuristic.

    Returns the starting index of pattern in text or -1.
    Time: O(n) average, Space: O(m)
    """
    m, n = len(pattern), len(text)
    if m == 0:
        return 0
    bad = {c: i for i, c in enumerate(pattern)}
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i
        i += max(1, j - bad.get(text[i + j], -1))
    return -1
