# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n=0
#         result=[]
#         for n in range(len(nums) - k + 1):
#             three=nums[n:n+k]
#             max1=max(three)
#             result.append(max1)
#         return result
#暴力解法：超时
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        q=deque()
        for i,x in enumerate(nums):
            #1、入
            while q and x>=nums[q[-1]]:
                q.pop()
            q.append(i)
            #2、出
            if i-q[0]>=k:
                q.popleft()
            #3、记录答案
            if i>=k-1:
                ans.append(nums[q[0]])
        return ans