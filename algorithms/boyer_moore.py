"""
Boyer-Moore string search algorithm.

This implementation of the Boyer-Moore algorithm finds the first occurrence of a
pattern in a text. It uses the bad-character heuristic to skip sections of the
text, which makes it faster than naive string search algorithms in practice.

Time Complexity: O(n*m) in the worst case, but O(n) on average, where n is the
length of the text and m is the length of the pattern.
Space Complexity: O(m), where m is the length of the pattern.
"""

def boyer_moore(text: str, pattern: str) -> int:
    """
    Boyer-Moore string search using the bad-character heuristic.

    Args:
        text: The text to search in.
        pattern: The pattern to search for.

    Returns:
        The starting index of the first occurrence of the pattern in the text,
        or -1 if the pattern is not found.
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

if __name__ == "__main__":
    text = "HERE IS A SIMPLE EXAMPLE"
    pattern = "EXAMPLE"
    index = boyer_moore(text, pattern)
    if index != -1:
        print(f'Pattern "{pattern}" found at index {index}')
    else:
        print(f'Pattern "{pattern}" not found')