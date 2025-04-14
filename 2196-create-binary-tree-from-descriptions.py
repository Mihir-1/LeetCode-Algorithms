# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        valToNode = {}
        children = set()
        
        # Build Tree
        for parent, child, isLeft in descriptions:
            children.add(child)
            if parent not in valToNode:
                valToNode[parent] = TreeNode(parent)
            if child not in valToNode:
                valToNode[child] = TreeNode(child)
            if isLeft:
                valToNode[parent].left = valToNode[child]
            else:
                valToNode[parent].right = valToNode[child]
        
        for nodeVal in valToNode.keys():
            if nodeVal not in children:
                return valToNode[nodeVal]
