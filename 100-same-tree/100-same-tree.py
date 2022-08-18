# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True
        
        def dfs(p, q):
            if not p and not q:
                return
            if (not p or not q) or (p.val != q.val):
                self.same = False
                return
            dfs(p.left, q.left)
            dfs(p.right, q.right)
        
        dfs(p, q)
        return self.same