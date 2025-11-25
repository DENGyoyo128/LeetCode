# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        cur=dummy

        #记录进位的情况
        carry=0

        while l1 or l2 or carry:
            a=l1.val if l1 else 0
            b=l2.val if l2 else 0

            s=a+b+carry
            digit=s%10
            carry=s//10

            cur.next=ListNode(digit)
            cur=cur.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        
        return dummy.next