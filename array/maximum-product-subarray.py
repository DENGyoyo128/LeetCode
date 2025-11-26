class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        dp_max=[0]*(n+1)
        dp_min=[0]*(n+1)
        dp_max[0]=dp_min[0]=ans=nums[0]

        for i in range(1,n):
            a=dp_max[i-1]*nums[i]
            b=dp_min[i-1]*nums[i]
            res=max(a,b)
            ans=max(ans,res)
        return ans
