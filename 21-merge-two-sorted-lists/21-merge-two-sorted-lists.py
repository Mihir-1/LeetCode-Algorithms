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
            print(res)
            print(p)
            print(list1)
            print(list2)
            if not list1:
                print("c1")
                p.next = list2
                p = p.next
                list2 = list2.next
            elif not list2:
                print("c2")
                p.next = list1
                p = p.next
                list1 = list1.next
            elif list1.val < list2.val:
                print("c3")
                p.next = list1
                p = p.next
                list1 = list1.next
            else:
                print("c4")
                p.next = list2
                p = p.next
                list2 = list2.next
            
        return res