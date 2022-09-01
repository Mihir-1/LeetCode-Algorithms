# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        q = deque([root])
        res = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                val = None
                if node:
                    val = node.val
                    q.append(node.left)
                    q.append(node.right)
                res.append(val)
        return str(res)
        
    def deserialize(self, data):
        data = deque(data[1:-1].split(", "))
        if data[0] == 'None':
            return None
        rootVal = data.popleft()
        root = TreeNode(int(rootVal))
        q = deque([root])
        while q:
            node = q.popleft()
            l = data.popleft()
            r = data.popleft()
            node.left = TreeNode(int(l)) if l != "None" else None
            node.right = TreeNode(int(r)) if r != "None" else None
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))