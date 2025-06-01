# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # Iterative DFS
        pseudoPals = 0
        stack = [(root, {root.val})]
        while stack:
            node, oddInstances = stack.pop()
            if not node.left and not node.right:
                if len(oddInstances) <= 1:
                    pseudoPals += 1

            if node.right: 
                rightOdds = oddInstances.copy()
                rightOdds.remove(node.right.val) if node.right.val in oddInstances else rightOdds.add(node.right.val)
                stack.append((node.right, rightOdds))
            if node.left:
                leftOdds = oddInstances.copy()
                leftOdds.remove(node.left.val) if node.left.val in oddInstances else leftOdds.add(node.left.val)
                stack.append((node.left, leftOdds))

        return pseudoPals

        """
        # Recursive DFS
        oddInstances = set()
        pseudoPals = 0

        def dfs(node):
            nonlocal pseudoPals
            oddInstances.remove(node.val) if node.val in oddInstances else oddInstances.add(node.val)
            
            # Base case: Leaf reached -> increment if pseudopal    
            if not node.left and not node.right:
                if len(oddInstances) <= 1:
                    pseudoPals += 1

            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
            oddInstances.remove(node.val) if node.val in oddInstances else oddInstances.add(node.val)                          

        dfs(root)
        return pseudoPals
        '''
        Time: O(n)
        Space: O(h) - call stack
                O(1) - auxillary 
        q: why int nonlocal and not set? understand nonlocal, and if param better


        * root to leaf paths -> dfs
        
        pseudo palindrome - rearrange to form palindrom
            - aka at most 1 number shows up odd times in path

        maintain set of odd counts, (new number: if in set remove, if not, add)
        increment res if len(set) <= 1 

        '''
        """
