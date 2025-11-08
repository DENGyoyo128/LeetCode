class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for x in nums:
            if x > target:  # 小剪枝：单个数超过 target 无法参与
                continue
            for j in range(target, x - 1, -1):
                dp[j] = dp[j] or dp[j - x]
        return dp[target]