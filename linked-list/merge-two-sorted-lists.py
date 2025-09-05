class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 创建虚拟头节点
        dummy = ListNode(0)
        curr = dummy
        
        # 遍历两个链表
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # 将剩余的链表直接连接上去
        curr.next = list1 if list1 else list2
        
        return dummy.next