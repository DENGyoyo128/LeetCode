class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set=set(nums)
        length=1
        for num in nums_set:
            if num-1 not in nums_set:
                num_start=num
                cur_length=1
                while num_start+1 in nums_set:
                    num_start+=1
                    cur_length+=1
                length=max(length,cur_length)
        return length