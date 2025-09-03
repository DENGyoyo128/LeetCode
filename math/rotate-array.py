
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        temp = nums[-k:] + nums[:-k]
        for i in range(n):
            nums[i] = temp[i]