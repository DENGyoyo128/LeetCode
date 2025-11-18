class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=0
        records=defaultdict(int)
        for num in nums:
            if num==k:
                ans+=1
            if k-num in records:
                ans+=1
            records[num]+=1
        return ans

#这道题难点我觉得是多个怎么办