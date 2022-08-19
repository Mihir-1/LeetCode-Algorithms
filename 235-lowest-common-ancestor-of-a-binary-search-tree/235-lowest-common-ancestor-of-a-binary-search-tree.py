# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if q.val < p.val:
            p, q = q, p
        
        stack = []
        if root: stack.append(root)
        while stack:
            node = stack.pop()
            if p.val <= node.val and node.val <= q.val:
                return node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)