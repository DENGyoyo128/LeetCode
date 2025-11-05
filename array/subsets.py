class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        n = len(nums)

        def dfs(start: int):
            # 任何时刻的 path 都是一个子集
            res.append(path.copy())
            for i in range(start, n):
                path.append(nums[i])   # 选择 nums[i]
                dfs(i + 1)             # 继续向右
                path.pop()             # 撤销选择

        dfs(0)
        return res