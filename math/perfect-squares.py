class Solution:
    def numSquares(self, n: int) -> int:
        
        # 预生成所有 <= n 的平方数
        squares = []
        k = 1
        while k * k <= n:
            squares.append(k * k)
            k += 1

        # dp[x]: 和为 x 的最少平方数个数
        dp = [0] + [10**9] * n
        for x in range(1, n + 1):
            for s in squares:
                if s > x:
                    break
                dp[x] = min(dp[x], dp[x - s] + 1)
        return dp[n]