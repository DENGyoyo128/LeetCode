class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        n=len(nums)
        used=[False]*n
        def dfs():
            if len(path)==len(nums):
                res.append(path.copy())
                return
            for i in range(n):
                num=nums[i]
                if used[i]:
                    continue
                used[i]=True
                path.append(nums[i])
                dfs()
                path.pop()
                used[i]=False
        dfs()
        return res




