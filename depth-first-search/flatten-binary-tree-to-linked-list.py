# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 中左右
        if not root:
            return
        
        stack = [root]
        prev = None
        
        while stack:
            node = stack.pop()
            
            if prev:
                prev.left = None
                prev.right = node
            
            # 注意：先右再左，保证前序
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
            prev = node