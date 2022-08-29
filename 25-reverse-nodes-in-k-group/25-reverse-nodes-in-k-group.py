# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.start = self.end = head
        head = self.past = ListNode(-1, self.start)
        
        while True:
            for _ in range(k - 1):
                if self.end:
                    self.end = self.end.next
            if not self.end:
                break
            self.reverseGroup()
            #print(head)
        return head.next
    
    def reverseGroup(self):
        p = ListNode(None)
        c = self.start
        while p is not self.end:
            n = c.next
            c.next = p
            p = c
            c = n
        self.past.next = p
        self.start.next = c
        self.past = self.start
        self.end = self.start = self.start.next
        return