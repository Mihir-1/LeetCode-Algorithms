from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            while q:
                cur = q.popleft()
                i, j = cur
                for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if (0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == '1' and (ni, nj) not in visited):
                        q.append((ni, nj))
                        visited.add((ni, nj))
        res = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    res += 1
        
        return res

        '''
        Time: O(m * n)
        Space: O(m * n)
        '''
