class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # ans=0
        # records=defaultdict(int)
        # for num in nums:
        #     if num==k:
        #         ans+=1
        #     if k-num in records:
        #         ans+=1
        #     records[num]+=1
        # return ans

        pre_sum=0
        ans=0
        records=defaultdict(int)
        records[0]=1
        for num in nums:
            pre_sum+=num
            if pre_sum-k in records:
                ans+=records[pre_sum-k]
            records[pre_sum]+=1
        return ans


#这道题难点我觉得是多个怎么办——用前缀和