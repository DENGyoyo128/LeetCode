class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #dp数组的含义dp[i][j]表示长度i（下标i-1为结尾）的word1和长度j（下标j-1位结尾）的word2的最少操作次数
        m=len(word1)
        n=len(word2)

        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(
                        dp[i-1][j]+1,
                        dp[i][j-1]+1,
                        dp[i-1][j-1]+1)
        return dp[m][n]