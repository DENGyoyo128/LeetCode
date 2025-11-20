class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        left=0
        right=len(nums)-1
        rp=1
        lp=1
        while left<n and right>=0:
            ans[left]*=lp
            ans[right]*=rp
            
            lp*=nums[left]
            rp*=nums[right]

            left+=1
            right-=1
            
        return ans
