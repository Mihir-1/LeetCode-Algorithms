# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        p = res
        carry = False
        
        while l1 or l2 or carry:
            total = 0
            if carry:
                total += 1
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
                
            carry = total >= 10
            p.next = ListNode(total % 10)
            p = p.next
            
        return res.next