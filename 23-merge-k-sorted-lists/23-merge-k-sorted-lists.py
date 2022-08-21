# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = [(l.val, i, l) for i, l in enumerate(lists) if l]
        heapq.heapify(minHeap)
        
        p = res = ListNode(0)
        while minHeap:
            val = heapq.heappop(minHeap)
            p.next = val[2]
            newNode = val[2].next
            if newNode:
                heapq.heappush(minHeap, (newNode.val, val[1], newNode))
            p = p.next
        
        return res.next
            