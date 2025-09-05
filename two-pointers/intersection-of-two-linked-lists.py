# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        ptrA = headA
        ptrB = headB
        
        while ptrA != ptrB:
            if ptrA:
                ptrA = ptrA.next
            else:
                ptrA = headB
                
            if ptrB:
                ptrB = ptrB.next
            else:
                ptrB = headA
                
        return ptrA