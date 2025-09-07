# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         #赌一波：双指针+虚拟头节点
#         if not head or head.next:
#             return head
#         dummy=ListNode(0)
#         curr=dummy
#         slow=head
#         fast=head.next
#         while fast and fast.next:
#             curr.next=fast
#             curr.next.next=slow
#             slow=slow.next.next
#             fast=fast.next.next
        
#         return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建虚拟头节点，简化操作
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # prev指向当前一对节点的前一个节点
        
        while prev.next and prev.next.next:
            # 定义当前一对节点
            first = prev.next
            second = prev.next.next
            
            # 交换节点
            first.next = second.next
            second.next = first
            prev.next = second
            
            # 移动prev到下一对的前一个节点（即当前的first，因为交换后first变为这一对的最后一个）
            prev = first
        
        return dummy.next

        