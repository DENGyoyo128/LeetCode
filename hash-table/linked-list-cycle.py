class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
      
        
        slow = head  # 慢指针，每次走一步
        fast = head  # 快指针，每次走两步
        
        while fast and fast.next:
            slow = slow.next        # 慢指针走一步
            fast = fast.next.next   # 快指针走两步
            
            if slow == fast:        # 如果相遇，说明有环
                return True
        
        return False  # 快指针到达末尾，说明无环