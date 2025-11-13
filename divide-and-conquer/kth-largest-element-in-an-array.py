class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)          # 建一个最小堆（容量 k）
        for x in nums[k:]:
            if x > h[0]:
                heapq.heapreplace(h, x)  # 用更大的替换堆顶
        return h[0]   