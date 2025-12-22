# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def depth(node):
            if not node:
                return -1  # 按“边数”计深度：空节点 -1，叶子节点 0
            left = depth(node.left)
            right = depth(node.right)

            # 经过 node 的最长路径边数
            self.ans = max(self.ans, left + right + 2)

            # 返回 node 往下的最大深度（边数）
            return 1 + max(left, right)
        depth(root)
        return self.ans