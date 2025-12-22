# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        size = len(nums)
        if size == 1:
            return TreeNode(nums[0])
        middle = size//2
        root = TreeNode(nums[middle])
        left = nums[0:middle]
        right = nums[middle+1:]
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)
        return root