# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        
        # 初始化两个指针
        ptrA, ptrB = headA, headB
        
        # 遍历直到两个指针相遇
        while ptrA != ptrB:
            # 如果ptrA到达末尾，切换到headB
            ptrA = ptrA.next if ptrA else headB
            # 如果ptrB到达末尾，切换到headA
            ptrB = ptrB.next if ptrB else headA
        
        # 返回相遇点（要么是交点，要么是None）
        return ptrA