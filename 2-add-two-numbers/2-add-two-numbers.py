# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        p1, p2, pr = l1, l2, res
        carry = False
        
        while p1 or p2:
            total = 0
            if carry:
                total += 1
            if p1:
                total += p1.val
                p1 = p1.next
            if p2:
                total += p2.val
                p2 = p2.next
                
            carry = total >= 10
            pr.next = ListNode(total % 10)
            pr = pr.next
        
        if carry:
            pr.next = ListNode(1)
            
        return res.next