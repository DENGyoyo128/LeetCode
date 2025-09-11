# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
#定义一个队列，如果root不为空，加入第一个节点
        queue = collections.deque([root])
        result = []
#当队列不为空，一直去遍历
        while queue:
#定义一维数组（当前层），一维数组循环结束之后，放入二维数组（最终结果集）
            level = []
#通过size控制本层的元素
            for _ in range(len(queue)):
#弹出元素，记录在一维数组里	
                cur = queue.popleft()
                level.append(cur.val)
#进入下一层队列里
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result