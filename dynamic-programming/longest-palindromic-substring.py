class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]
        start, maxlen = 0, 1

        for i in range(n - 1, -1, -1):
            dp[i][i] = True  # 单字符
            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > maxlen:
                        start, maxlen = i, j - i + 1

        return s[start:start + maxlen]