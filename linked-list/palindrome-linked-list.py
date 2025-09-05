class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        # 步骤1：使用快慢指针找到中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 步骤2：反转后半部分链表
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # 步骤3：比较前半部分和反转后的后半部分
        first_half = head
        second_half = prev  # prev现在是反转后的后半部分的头节点
        
        while second_half:  # 只需要比较到后半部分结束
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True