# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r1, r2):
            if not r1 and not r2:
                return True
            if (not r1 or not r2) or (r1.val != r2.val):
                return False
            return isSame(r1.left, r2.left) and isSame(r1.right, r2.right)
        
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if isSame(node, subRoot):
                    return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False