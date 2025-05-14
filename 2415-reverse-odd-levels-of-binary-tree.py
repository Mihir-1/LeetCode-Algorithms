from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        q = deque([root])
        oddLevel = False

        while q:
            width = len(q)
            if oddLevel:      
                for i in range(width // 2):
                    q[i].val, q[width - i - 1].val = q[width - i - 1].val, q[i].val

            for _ in range(width):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            oddLevel = not oddLevel

        return root
        '''
        Time: O(n)
        Space: O(n)
        '''
