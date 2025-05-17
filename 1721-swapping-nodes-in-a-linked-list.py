# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Find length
        cur = head
        size = 1
        while cur.next:
            cur = cur.next
            size += 1
        
        # Find kth node
        cur = head
        count = 1
        while count < k:
            cur = cur.next
            count += 1
        left = cur
        

        # Find len-kth node 
        cur = head
        count = 1
        while count < size - k + 1:
            cur = cur.next
            count += 1
        right = cur

        left.val, right.val = right.val, left.val
        return head
        '''  
        Time: O(n)
        Space: O(1)
        '''
        
