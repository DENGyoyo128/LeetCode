# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxVal = float('-inf')  # 因为后台测试数据中有int最小值

    def isValidBST(self, root):
        if root is None:
            return True

        left = self.isValidBST(root.left)
        # 中序遍历，验证遍历的元素是不是从小到大
        if self.maxVal < root.val:
            self.maxVal = root.val
        else:
            return False
        right = self.isValidBST(root.right)

        return left and right