# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f = s = ListNode(-1, head)
        head = f
        
        while n > 0:
            f = f.next
            n -= 1
        
        while f.next:
            f = f.next
            s = s.next
            
        s.next = s.next.next
        
        return head.next