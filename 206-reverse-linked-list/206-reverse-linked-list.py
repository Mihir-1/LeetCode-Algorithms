# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if (head is None or head.next is None):
            return head
        p = head
        c = head.next
        head.next = None
        while (c):
            head = c
            c = c.next
            head.next = p
            p = head
        return head
        