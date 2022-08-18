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
                return True
            if (not p or not q) or (p.val != q.val):
                self.same = False
                return False 
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        
        return dfs(p, q)