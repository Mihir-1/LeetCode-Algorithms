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
        
        cur = root
            
        while True:
            if p.val > cur.val:
                cur = cur.right
            elif q.val < cur.val:
                cur = cur.left
            else:
                return cur