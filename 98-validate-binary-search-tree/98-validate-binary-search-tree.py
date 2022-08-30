# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        if root:
            stack.append((root, float("-inf"), float("inf")))
            
        while stack:
            val = stack.pop()
            node, low, high = val[0], val[1], val[2]
            if not (low < node.val and node.val < high):
                return False
            if node.right:
                stack.append((node.right, max(low, node.val), high))
            if node.left:
                stack.append((node.left, low, min(high, node.val)))
                
        return True