class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort() # 先排序
        n = len(nums)
        # 每次跳两个元素进行检查
        for i in range(0, n - 1, 2):
            # 如果当前元素和下一个元素不相等
            if nums[i] != nums[i + 1]:
                return nums[i] # 当前元素就是单身数字
        # 如果前面的循环都没返回，说明单身数字是最后一个元素
        return nums[-1]
