                
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        freq = defaultdict(int)
        freq[0] = 1   # 前缀和等于 k 时也能统计到

        for num in nums:
            prefix_sum += num
            # 如果 prefix_sum - k 在 freq 里，说明存在子数组和为 k
            count += freq[prefix_sum - k]
            freq[prefix_sum] += 1
        
        return count