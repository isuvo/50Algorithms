"""
Longest Common Subsequence (LCS).

This implementation of the LCS algorithm finds the longest subsequence that is
common to two strings. A subsequence is a sequence that can be derived from
another sequence by deleting some or no elements without changing the order of
the remaining elements. It uses dynamic programming to store the lengths of
the longest common subsequences of all prefixes of the two strings.

Time Complexity: O(n*m), where n and m are the lengths of the two strings.
Space Complexity: O(n*m), where n and m are the lengths of the two strings.
"""

def lcs(a: str, b: str) -> str:
    """
    Return the longest common subsequence of strings a and b.

    Args:
        a: The first string.
        b: The second string.

    Returns:
        The longest common subsequence of the two strings.
    """
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if a[i] == b[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    i = j = 0
    res = []
    while i < n and j < m:
        if a[i] == b[j]:
            res.append(a[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1
    return "".join(res)

if __name__ == "__main__":
    string1 = "AGGTAB"
    string2 = "GXTXAYB"
    common_subsequence = lcs(string1, string2)
    print(f'The longest common subsequence of "{string1}" and "{string2}" is "{common_subsequence}"')