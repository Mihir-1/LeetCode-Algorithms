"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = dict()
    
        def dfs(node):
            if node in visited:
                return visited[node]
            print(node.val, node)
            newNode = Node(node.val)
            visited.update({node : newNode})
            for nd in node.neighbors:
                newNode.neighbors.append(dfs(nd))
            return newNode
        
        return dfs(node) if node else None
        