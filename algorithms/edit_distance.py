"""
Levenshtein edit distance between two strings.

This implementation of the Levenshtein edit distance algorithm calculates the
minimum number of single-character edits (insertions, deletions, or
substitutions) required to change one string into the other. It uses dynamic
programming to store the edit distances between all prefixes of the two
strings.

Time Complexity: O(n*m), where n and m are the lengths of the two strings.
Space Complexity: O(n*m), where n and m are the lengths of the two strings.
"""

def edit_distance(a: str, b: str) -> int:
    """
    Compute the Levenshtein edit distance between strings a and b.

    Args:
        a: The first string.
        b: The second string.

    Returns:
        The Levenshtein edit distance between the two strings.
    """
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # Deletion
                dp[i][j - 1] + 1,  # Insertion
                dp[i - 1][j - 1] + cost,  # Substitution
            )
    return dp[n][m]

if __name__ == "__main__":
    string1 = "kitten"
    string2 = "sitting"
    distance = edit_distance(string1, string2)
    print(f'The edit distance between "{string1}" and "{string2}" is {distance}')