"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        # Optimal
        
        leaf_node = {
            0: Node(False, True),
            1: Node(True, True)
        }
      
        # row & col refer to idx of top-left node
        # size: length of sub-grid
        def constructTree(row, col, size):
            # Base Case: One Cell in sub-grid
            if size == 1:
                return leaf_node[grid[row][col]]

            # Recurse over sub-grids
            next_size = size / 2
            tl = constructTree(row, col, next_size)
            tr = constructTree(row, col + next_size, next_size)
            bl = constructTree(row + next_size, col, next_size)
            br = constructTree(row + next_size, col + next_size, next_size)

            # All sub-grids same - no reference to sub-grid
            if ((tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf)
                and (tl.val == tr.val == bl.val == br.val)):
                return tl

            return Node(True, False, tl, tr, bl, br)


        size = len(grid[0])
        return constructTree(0, 0, size)


        '''
        Runtime: O(n^2)
        Space: O(log n)
        '''



        """
        # Brute Force
        # row & col refer to idx of top-left node
        # size: length of sub-grid
        def constructTree(row, col, size):
            # Check if all vals within sub-grid are same
            top_left = grid[row][col]
            all_same = True
            for r in range(row, row + size):
                for c in range(col, col + size):
                    if grid[r][c] != top_left:
                        all_same = False

            # Base Case: All nodes within sub-grid contain same value
            if all_same:
                return Node(bool(top_left), True)

            # Recurse
            next_size = size / 2
            node = Node()
            node.topLeft = constructTree(row, col, next_size)
            node.topRight = constructTree(row, col + next_size, next_size)
            node.bottomLeft = constructTree(row + next_size, col, next_size)
            node.bottomRight = constructTree(row + next_size, col + next_size, next_size)
            return node

        size = len(grid[0])
        return constructTree(0, 0, size)


        '''
        Runtime: O(n^2 * log n)
        Space: O(log n)
        '''
        """
