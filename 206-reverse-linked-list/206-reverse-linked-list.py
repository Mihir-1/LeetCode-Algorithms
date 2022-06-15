# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if (not head or not head.next):
            return head
        p = None
        while head:
            c = head.next
            head.next = p
            p = head
            head = c
        return p
        