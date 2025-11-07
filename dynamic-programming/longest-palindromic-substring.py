class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # dp[i][j]：s[i..j] 是否是回文子串
        dp = [[False] * n for _ in range(n)]

        start, maxlen = 0, 1
        # 长度为 1
        for i in range(n):
            dp[i][i] = True

        # 长度为 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start, maxlen = i, 2

        # 长度 >= 3
        for L in range(3, n + 1):                   # 子串长度
            for i in range(0, n - L + 1):
                j = i + L - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if L > maxlen:
                        start, maxlen = i, L

        return s[start:start + maxlen]