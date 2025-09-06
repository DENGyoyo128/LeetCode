# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建虚拟头节点，简化头节点删除操作
        dummy = ListNode(0)
        dummy.next = head
        
        # 初始化快慢指针
        fast = dummy
        slow = dummy
        
        # 快指针先移动n步
        for i in range(n+1):
            fast = fast.next
        
        # 快慢指针同时移动，直到快指针到达末尾
        while fast:
            fast = fast.next
            slow = slow.next
        
        # 删除倒数第n个节点（slow.next）
        slow.next = slow.next.next
        
        return dummy.next