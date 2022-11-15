# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        leftQ = deque([(False, root)])
        while leftQ:
            left, node = leftQ.popleft()
            if left and not node.left and not node.right:
                total += node.val
            if node.left:
                leftQ.append((True, node.left))
            if node.right:
                leftQ.append((False, node.right))
        return total