# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS - inorder
        stack = []
        cur = root
        prev = None
        minDiff = float('inf')

        while stack or cur:
            # Explore left sub-tree
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            if prev:
                minDiff = min(cur.val - prev.val, minDiff)
            prev = cur
            cur = cur.right

        return minDiff
        '''
        Time: O(n)
        Space: O(n)
        '''

        """
        # Recursive DFS - inorder
        minDiff = float('inf')
        prev = None

        def dfs(node):
            if not node:
                return
            nonlocal prev, minDiff

            dfs(node.left)
            if prev:
                minDiff = min(node.val - prev.val, minDiff)

            prev = node
            dfs(node.right)

        dfs(root)
        return minDiff
        '''
        Time: O(n)
        Space: O(n)
        '''
        """
