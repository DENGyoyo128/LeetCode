"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 1) 旧节点 -> 新节点 的映射
        mp = {}
        
        cur = head
        while cur:
            mp[cur] = Node(cur.val)
            cur = cur.next
        
        # 2) 补 next 和 random
        cur = head
        while cur:
            new_node = mp[cur]
            new_node.next = mp.get(cur.next)      # cur.next 可能是 None
            new_node.random = mp.get(cur.random)  # cur.random 可能是 None
            cur = cur.next
        
        # 3) 返回新链表的头
        return mp[head]
        