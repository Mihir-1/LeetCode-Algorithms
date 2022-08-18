# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        
        def dfs(root):
            if not root:
                return -1
            
            lh = dfs(root.left)
            rh = dfs(root.right)
            
            self.maxD = max(self.maxD, lh + rh + 2)
            
            return 1 + max(lh, rh)
        
        dfs(root)
        return self.maxD