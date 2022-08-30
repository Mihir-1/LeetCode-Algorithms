# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        if root:
            stack.append((root, root.val))
        good = 0
        
        while stack:
            node = stack.pop()
            node, nodeMax = node[0], node[1]
            if nodeMax == node.val:
                good += 1
            if node.right:
                stack.append((node.right, max(node.right.val, nodeMax)))
            if node.left:
                stack.append((node.left, max(node.left.val, nodeMax)))
        
        return good