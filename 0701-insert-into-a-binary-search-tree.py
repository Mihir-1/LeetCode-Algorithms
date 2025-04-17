# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
      
        # Iterative Solution
        
        if not root:
            return TreeNode(val)

        cur = root
        while True:
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
        

        '''
        # Recursive Solution

        # Base Case: Insertion point found
        if not root:
            return TreeNode(val)
        
        # Recursion: Search for insertion point
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root
        '''

        '''
        h = height of tree
        Runtime: O(h) -> worst case: O(n)
        Space: O(h) -> worst case: O(n)
        '''
