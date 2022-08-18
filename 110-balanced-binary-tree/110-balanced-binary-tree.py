# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return (True, 0)
            
            l, r = dfs(root.left), dfs(root.right)
            bal = l[0] and r[0] and abs(l[1] - r[1]) <= 1
            return (bal, 1 + max(l[1], r[1]))

        return dfs(root)[0]