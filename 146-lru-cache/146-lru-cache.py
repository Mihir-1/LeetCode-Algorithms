class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.lru, self.mru = Node(-1, -1), Node(-2, -2)
        self.lru.next, self.mru.prev = self.mru, self.lru
        self.capacity = capacity
        self.nodeMap = {}
    
    def remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p
    
    def insert(self, node):
        p = self.mru.prev
        p.next = self.mru.prev = node
        node.prev, node.next = p, self.mru

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap.get(key)   
        # remove node from ll and repair
        self.remove(node)
        
        # insert node to prev of mru
        self.insert(node)
        
        # return node.val
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            # remove node from ll and repair
            node = self.nodeMap.get(key)
            self.remove(node)
            # update value
            node.val = value
        else:
            if len(self.nodeMap) == self.capacity:
                # remove node next of lru
                node = self.lru.next
                self.remove(self.lru.next)
                # remove key from nodeMap
                self.nodeMap.pop(node.key)
            # create node
            node = Node(key, value)
            # put key in nodeMap
            self.nodeMap.update({key: node})
        # insert node prev of mru
        self.insert(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)