# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        if list1.val < list2.val:
            res = list1
            list1 = list1.next
        else:
            res = list2
            list2 = list2.next
        p = res
        
        while list1 or list2:
            if not list1:
                p.next = list2
                p = p.next
                list2 = list2.next
            elif not list2:
                p.next = list1
                p = p.next
                list1 = list1.next
            elif list1.val < list2.val:
                p.next = list1
                p = p.next
                list1 = list1.next
            else:
                p.next = list2
                p = p.next
                list2 = list2.next
            
        return res