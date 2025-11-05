class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(start: int, remain: int):
            if remain == 0:
                res.append(path.copy())
                return
            for i in range(start, len(candidates)):
                x = candidates[i]
                if x > remain:      # 剪枝：后面更大，直接停
                    break
                path.append(x)
                dfs(i, remain - x)  # 可重复使用同一元素 → 仍从 i 开始
                path.pop()

        dfs(0, target)
        return res