# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = end = head
        head = past = ListNode(-1, start)
        
        while True:
            i = k - 1
            while i > 0:
                if not end:
                    return head.next
                end = end.next
                i -= 1
            if not end:
                break

            p = ListNode(None)
            c = start
            
            while p is not end:
                n = c.next
                c.next = p
                p, c = c, n
            past.next = p
            start.next = c
            past = start
            end = start = start.next
        return head.next