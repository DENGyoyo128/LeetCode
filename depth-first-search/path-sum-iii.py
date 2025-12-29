# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1  # 空前缀：方便处理“从根开始”的路径

        def dfs(node, cur_sum):
            if not node:
                return 0
            cur_sum += node.val
   # 以当前节点为结尾的、满足 targetSum 的路径条数
            res = cnt[cur_sum - targetSum]

            # 记录当前前缀和
            cnt[cur_sum] += 1

            # 继续往下
            res += dfs(node.left, cur_sum)
            res += dfs(node.right, cur_sum)

            # 回溯：撤销当前节点的贡献
            cnt[cur_sum] -= 1
            return res
        return dfs(root, 0)