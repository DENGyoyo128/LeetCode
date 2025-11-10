class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        # 找到第一个 >= target 的位置
        def lower_bound():
            l, r = 0, n
            while l < r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l

        # 找到第一个 > target 的位置
        def upper_bound():
            l, r = 0, n
            while l < r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m
                else:
                    l = m + 1
            return l

        L = lower_bound()
        if L == n or nums[L] != target:
            return [-1, -1]
        R = upper_bound() - 1

        return [L, R]