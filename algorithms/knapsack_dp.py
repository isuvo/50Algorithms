"""
0/1 Knapsack problem solved using dynamic programming.

This implementation of the 0/1 knapsack problem finds the maximum value that
can be put in a knapsack of a given capacity. It uses dynamic programming to
store the maximum value that can be achieved with each capacity from 0 to the
target capacity.

Time Complexity: O(n*W), where n is the number of items and W is the capacity
of the knapsack.
Space Complexity: O(n*W), where n is the number of items and W is the capacity
of the knapsack.
"""
from typing import List

def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """
    0/1 knapsack solved via dynamic programming.

    Args:
        weights: A list of weights of the items.
        values: A list of values of the items.
        capacity: The capacity of the knapsack.

    Returns:
        The maximum value that can be put in the knapsack.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

if __name__ == "__main__":
    weights = [1, 2, 3]
    values = [6, 10, 12]
    capacity = 5
    max_value = knapsack(weights, values, capacity)
    print(f"The maximum value that can be put in the knapsack is {max_value}")