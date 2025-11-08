class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = float('inf')
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for c in coins:
            for x in range(c, amount + 1):
                dp[x] = min(dp[x], dp[x - c] + 1)

        return -1 if dp[amount] == inf else dp[amount]