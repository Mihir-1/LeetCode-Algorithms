# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Simple Solution
        res = []
        stack = []
        cur = root
        while cur or stack:
            # Explore left branch
            while cur:
                stack.append(cur)
                cur = cur.left

            # Add Node and shift to right branch
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res

        # Flexible Solution
        '''
        res = []
        stack = [(root, False)] # Tuple: (Node, has_been_visited)

        while stack:
            node, visited = stack.pop()
            if node:
                if visited: 
                    res.append(node.val)
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))

        return res
        '''

'''
Time: O(n)
Space: O(n)
'''
