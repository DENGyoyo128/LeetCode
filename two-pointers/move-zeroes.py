class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left=0
        # right=len(nums)-1
        # while left<right:
        #     if nums[left]=0:
        #         nums[left],nums[right]=nums[right],nums[left]
        # 1) 先把所有非零元素“稳定地挤到前面”
        # 2) 剩下的位置全部填 0
        slow=0
        n=len(nums)
        for fast in range(n):
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1
        while slow < n:
            nums[slow]=0
            slow+=1
