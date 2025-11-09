class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        end = 0
        farthest = 0

        for i in range(n - 1):           # 到倒数第二个就行
            farthest = max(farthest, i + nums[i])
            if i == end:                 # 本跳的覆盖区间到头了
                jumps += 1
                end = farthest
                if end >= n - 1:         # 已经覆盖到终点，提前结束
                    break
        return jumps
