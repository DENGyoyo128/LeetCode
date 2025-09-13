# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        # 前序遍历的第一个就是根节点
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 在中序遍历中找到根的位置
        separator_idx = inorder.index(root_val)

        # 切割中序：左子树 / 右子树
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]

        # 切割前序：根节点之后，按左子树长度划分
        preorder_left = preorder[1: 1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]

        # 递归构建
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root