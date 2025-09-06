class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # 虚拟头节点
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # 获取当前节点的值，如果节点不存在则为0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 计算当前位的和（包括进位）
            total = val1 + val2 + carry
            carry = total // 10  # 更新进位
            digit = total % 10   # 当前位的数字
            
            # 创建新节点并移动指针
            curr.next = ListNode(digit)
            curr = curr.next
            
            # 移动l1和l2的指针（如果存在）
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next