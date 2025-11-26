class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        dp_max=[0]*(n+1)
        dp_min=[0]*(n+1)
        dp_max[0]=dp_min[0]=ans=nums[0]

        for i in range(1,n):
            a=dp_max[i-1]*nums[i]
            b=dp_min[i-1]*nums[i]
            dp_max[i]=max(nums[i],a,b)
            dp_min[i]=min(nums[i],a,b)
            ans=max(ans,dp_max[i])
        return ans
