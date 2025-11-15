class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    #   nums.sort()
    #   ans=[]
    #   n=len(nums)
    #   for i in range(n-2):
    #     x=nums[i]
    #     #如果跟上一数是相等的，跳过
    #     if i>0 and x==nums[i-1]:
    #       continue
    #     j=i+1
    #     k=n-1
    #     while j<k:
    #       s=x+nums[j]+nums[k]
    #       if s>0:
    #         k-=1
    #       elif s<0:
    #         j+=1
    #       else:
    #         ans.append([x,nums[j],nums[k]])
    #         #把j和k重复的也跳过
    #         while j<k and nums[j]==nums[j-1]:
    #           j+=1
    #         while j>k and nums[k]==nums[k+1]:
    #           k-=1
    #         j+=1
    #         k-=1
    #   return ans
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # 第一位去重：同样的 nums[i] 只用一次作为起点
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # 第二位去重
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # 第三位去重
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < 0:
                    left += 1
                else:  # s > 0
                    right -= 1

        return res