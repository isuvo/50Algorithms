def coin_change(coins, amount):
    """Minimum coins to make up amount using given coin denominations.

    Time: O(n*amount), Space: O(amount)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
    return dp[amount] if dp[amount] != float('inf') else -1
