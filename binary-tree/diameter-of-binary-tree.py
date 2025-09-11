# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def getdepth(node):
            if not node:
                return 0
            left = getdepth(node.left)
            right = getdepth(node.right)
            # 更新直径：经过当前节点的路径长度
            self.diameter = max(self.diameter, left + right)
            # 返回深度
            return 1 + max(left, right)

        getdepth(root)
        return self.diameter