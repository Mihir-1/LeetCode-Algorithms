# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        endOne = list1
        for _ in range(a - 1):
            endOne = endOne.next
        rmv = endOne.next
        for _ in range(b - a):
            rmv = rmv.next
        startTwo = rmv.next
        endOne.next = list2
        while endOne.next:
            endOne = endOne.next
        endOne.next = startTwo
        return list1