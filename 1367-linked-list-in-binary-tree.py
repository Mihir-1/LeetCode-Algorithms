from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def validPath(h, r):
            stack = [(h, r)]
            while stack:
                l, t = stack.pop()
                if l.next == None:
                    return True
                if l.next and t.left and l.next.val == t.left.val:
                    stack.append((l.next, t.left))
                if l.next and t.right and l.next.val == t.right.val:
                    stack.append((l.next, t.right))
            return False

        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == head.val and validPath(head, node):
                return True
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
        return False
