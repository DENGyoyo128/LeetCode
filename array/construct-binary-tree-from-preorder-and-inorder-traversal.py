# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}  # 哈希：值 -> 在 inorder 的下标
        self.pre_i = 0  # 当前用到 preorder 的第几个元素（指针）

        def build(in_l, in_r):
            if in_l > in_r:
                return None

            root_val = preorder[self.pre_i]  # 前序当前第一个就是根
            self.pre_i += 1
            root = TreeNode(root_val)

            mid = pos[root_val]              # O(1) 找根在 inorder 的位置
            root.left = build(in_l, mid - 1)
            root.right = build(mid + 1, in_r)
            return root

        return build(0, len(inorder) - 1)
