class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        left=0
        right=len(height)-1
        #这两个指针还没有相遇，还可以构成面积
        while left<right:
            area=(right-left)*min(height[left],height[right])
            ans=max(ans,area)
            #如果说左边矮，就把左边去掉，右边矮，就把右边去掉
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans