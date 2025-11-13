class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)          # 建一个最小堆（容量 k）
        for n in nums[k:]:
            heappushpop(heap, n)
        return heap[0]

    # O(nlgn) time
# def findKthLargest1(self, nums, k):
#     return sorted(nums, reverse=True)[k-1]