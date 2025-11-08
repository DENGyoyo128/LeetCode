class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n
        dp_max[0] = dp_min[0] = ans = nums[0]

        for i in range(1, n):
            x = nums[i]
            a = dp_max[i - 1] * x
            b = dp_min[i - 1] * x
            dp_max[i] = max(x, a, b)
            dp_min[i] = min(x, a, b)
            ans = max(ans, dp_max[i])
        return ans