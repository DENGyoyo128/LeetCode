class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)
        ans=0
        while left<right:
            area=min(height[left],height[right])*(right-left)
            ans=max(ans,area)
        return ans
            
        