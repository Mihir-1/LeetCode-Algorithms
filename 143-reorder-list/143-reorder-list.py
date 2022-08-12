# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Split LL
        s = f = ListNode(0, head)
        while f and f.next:
            s = s.next
            f = f.next.next
        b = s.next
        s.next = None
        
        # 2. Reverse b
        p = None
        while b:
            n = b.next
            b.next = p
            p = b
            b = n
        
        # 3. Splice head & b
        a = head
        b = p
        l = head
        while b:
            a = a.next
            l.next = b
            l = l.next
            b = b.next
            l.next = a
            l = l.next
