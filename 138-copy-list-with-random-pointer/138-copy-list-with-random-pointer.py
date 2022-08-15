"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}
        p = head
        while p:
            n = Node(p.val)
            oldToNew[p] = n
            p = p.next
        oldToNew[None] = None
        
        p = head
        while p:
            n = oldToNew[p]
            n.next = oldToNew[p.next]
            n.random = oldToNew[p.random]
            p = p.next
            
        return oldToNew[head]
            