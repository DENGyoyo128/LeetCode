class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        # 1) 找拐点 i：从右往左第一个 nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 如果没找到，说明是最大排列，直接反转成最小
        if i < 0:
            nums.reverse()
            return

        # 2) 从右往左找第一个 nums[j] > nums[i]，交换
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

        # 3) 反转 i+1 到末尾，让后缀变成最小（升序）
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1