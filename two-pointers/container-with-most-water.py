class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left=0
        # right=len(height)-1
        # ans=0
        # while left<right:
        #     area=min(height[left],height[right])*(right-left)
        #     ans=max(ans,area)
        #     left+=1
        #     right-=1
        # return ans
            
#“面积由短板决定 → 谁短就动谁”，不要两个指针一起往里缩。

        left = 0
        right = len(height) - 1
        ans = 0

        while left < right:
            h = min(height[left], height[right])
            area = h * (right - left)
            ans = max(ans, area)

            # 只移动短的那一侧
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans