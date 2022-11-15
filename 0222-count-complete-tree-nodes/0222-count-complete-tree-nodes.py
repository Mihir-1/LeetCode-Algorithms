# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        def getDepth(node):
            d = 0
            while node.left:
                node = node.left
                d += 1
            return d
        
        depth = getDepth(root)
        total = 0
        for i in range(depth + 1):
            total += 2 ** i
        temp = root
        while temp.left:
            depth -= 1            
            if not temp.right or getDepth(temp.left) > getDepth(temp.right):
                temp = temp.left
                total -= 2 ** depth
            else:
                temp = temp.right

        return total