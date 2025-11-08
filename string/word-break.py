class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        if not word_set:
            return False

        minL = min(len(w) for w in word_set)
        maxL = max(len(w) for w in word_set)

        dp = [False] * (n + 1)
        dp[0] = True  # 空串可切分

        for i in range(1, n + 1):
            # 只枚举可能长度
            for L in range(minL, maxL + 1):
                j = i - L
                if j < 0:
                    break
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]