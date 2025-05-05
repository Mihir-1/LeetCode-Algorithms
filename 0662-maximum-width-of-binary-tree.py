from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Iterative BFS
        maxWidth = 0
        q = deque([(root, 0)])
        
        while q:
            left = q[0][1]
            right = q[-1][1]
            for _ in range(len(q)):
                node, pos = q.popleft()
                if node.left:
                    q.append((node.left, 2 * pos))
                if node.right:
                    q.append((node.right, 2 * pos + 1))

            maxWidth = max(maxWidth, right - left + 1)

        return maxWidth


  '''
  Time: O(n)
  Space: O(n)
  '''
