class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        conse_length=1
        for num in nums_set:
            if num-1 not in nums_set:
                num_start=1
                cur_length=1
                while num+1 in nums_set:
                    num+=1
                    conse_length+=1
                    length=max(cur_length,conse_length)
        return length