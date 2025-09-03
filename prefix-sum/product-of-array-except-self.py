# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans = [1] * n
        
#         # 先计算每个元素左边的乘积，并存入ans
#         left = 1
#         for i in range(n):
#             ans[i] = left
#             left *= nums[i]
        
#         # 再计算每个元素右边的乘积，并乘以ans中已有的左边乘积
#         right = 1
#         for i in range(n-1, -1, -1):
#             ans[i] *= right
#             right *= nums[i]
        
#         return ans


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        left, right = 0, n - 1
        lp, rp = 1, 1  # lp: 左乘积累积, rp: 右乘积累积
        
        while left < n and right >= 0:
            # 更新左右指针位置的答案
            answer[left] *= lp
            answer[right] *= rp
            
            # 更新左右乘积累积
            lp *= nums[left]
            rp *= nums[right]
            
            # 移动指针
            left += 1
            right -= 1
        
        return answer

        