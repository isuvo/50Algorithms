"""
Coin change problem using dynamic programming.

This implementation of the coin change problem finds the minimum number of coins
required to make a certain amount of money. It uses dynamic programming to
store the minimum number of coins required to make each amount from 0 to the
target amount.

Time Complexity: O(n*a), where n is the number of coin denominations and a is
the target amount.
Space Complexity: O(a), where a is the target amount.
"""
from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    """
    Minimum coins to make up amount using given coin denominations.

    Args:
        coins: A list of coin denominations.
        amount: The target amount.

    Returns:
        The minimum number of coins required to make the target amount, or -1
        if the amount cannot be made up.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    min_coins = coin_change(coins, amount)
    if min_coins != -1:
        print(f"Minimum coins to make amount {amount} is {min_coins}")
    else:
        print(f"Amount {amount} cannot be made with the given coins")