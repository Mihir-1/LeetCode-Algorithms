class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # DSU
        parents = [i for i in range(n)]
        rank = [1] * n

        def find(u):
            if u != parents[u]:
                parents[u] = find(parents[u])

            return parents[u]

        def union(u, v):
            parents[v] = u
            rank[u] += rank[v]
        
        merges = 0

        for u, v in edges:
            ru = find(u)
            rv = find(v)
            if ru != rv: 
                union(ru, rv) if rank[rv] <= rank[ru] else union(rv, ru)
                merges += 1
        
        return n - merges
        '''
        Time: O(V + E)
        Space: O(E)
        '''

        """
        # DFS
        adj = [[] for _ in range(n)]
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)

        groups = 0

        for node in range(n):
            if not visited[node]:
                dfs(node)
                groups += 1

        return groups
        Time: O(V + E)
        Space: O(V + E)
        """
