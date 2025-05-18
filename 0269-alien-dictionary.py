class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {ord(c) - 97: set() for w in words for c in w}
        for i in range(len(words) - 1): 
            w1 = words[i]
            w2 = words[i + 1]
            limit = min(len(w1), len(w2))
            if w1[:limit] == w2[:limit] and len(w1) > len(w2):
                return ''

            for j in range(limit):
                # order found
                if w1[j] != w2[j]:
                    adj[ord(w1[j]) - 97].add(ord(w2[j]) - 97)
                    break

        res = []
        cur = set()
        visited = set()
        def dfs(node):
            # Explored node
            if node in visited:
                return False
            # Cycle found
            if node in cur:
                return True
            
            cur.add(node)
            for child in adj[node]:
                if dfs(child):
                    return True
            cur.remove(node)
            visited.add(node)
            res.append(chr(node + 97))

        for node in adj:
            if dfs(node):
                return ''

        return ''.join(reversed(res))
        '''
        Time: O(N)
        Space: O(V + E)
        '''
