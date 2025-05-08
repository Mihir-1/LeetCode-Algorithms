from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        oddLevel = False

        while q:
            prev = float('-inf')
            for _ in range(len(q)):
                node = q.popleft()
                val = -1 * node.val if oddLevel else node.val
                
                if val <= prev or val % 2 - int(not oddLevel) != 0:
                    return False

                prev = val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            oddLevel = not oddLevel
                
        return True
