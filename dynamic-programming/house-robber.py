class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n
        dp[0]=ans=nums[0]
        for i in range(1,n):
            dp[i]=dp[i-2]+nums[i]
            ans=max(ans,dp[i])
        return ans