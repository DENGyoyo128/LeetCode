# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1   # 空路径和为 0 出现一次
        self.ans = 0

        def dfs(node, cur_sum):
            if not node:
                return

            cur_sum += node.val
            # 以当前节点为终点、和为 targetSum 的路径条数
            self.ans += prefix[cur_sum - targetSum]

            # 当前前缀和计数 +1
            prefix[cur_sum] += 1

            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)

            # 回溯：离开该节点，前缀和计数 -1
            prefix[cur_sum] -= 1

        dfs(root, 0)
        return self.ans