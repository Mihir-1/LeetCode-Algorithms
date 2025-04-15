# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        res = [] # Resulting list
        stack = [(root, False)] # Tuple (node, children_visited{for close brackets})

        while stack:
            node, children_visited = stack.pop()

            if children_visited: # Finished exploring subtree
                res.append(')')
            else:
                res.append('(' + str(node.val))
                stack.append((node, True)) # Add parent to stack -> revisit to close parenthesis
                
                # Edge case: Right child but no left child
                if not node.left and node.right:
                    res.append('()')

                # Add children to stack
                if node.right: 
                    stack.append((node.right, False))
                if node.left: 
                    stack.append((node.left, False))

        return ''.join(res)[1:-1]


"""
Time: Each node processed twice: O(n)
Space: Stack size and res grows linearly with number of nodes: O(n)
"""











