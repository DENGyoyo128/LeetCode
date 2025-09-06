# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归终止条件：空链表或只有一个节点
        if not head or not head.next:
            return head
        
        # 使用快慢指针找到中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 分割链表
        mid = slow.next
        slow.next = None  # 切断链表
        
        # 递归排序左右两部分
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # 合并两个已排序的链表
        return self.merge(left, right)
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        # 连接剩余部分
        curr.next = l1 if l1 else l2
        
        return dummy.next
