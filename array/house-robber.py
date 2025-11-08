class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n
        dp[0]=ans=nums[0]
        for i in range(1,n):
            a=dp[i-2]
            dp[i]=max(dp[i-1],a+nums[i])
            ans=max(ans,dp[i])
        return ans