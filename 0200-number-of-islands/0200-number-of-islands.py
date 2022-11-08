class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        q = deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    q.append((i, j))
                    islands += 1
                while q:
                    r, c = q.popleft()
                    if (r, c) not in visited:
                        visited.add((r, c))
                        if 0 <= r + 1 < rows and (r + 1, c) not in visited and grid[r + 1][c] == "1": q.append((r + 1, c))
                        if 0 <= r - 1 < rows and (r - 1, c) not in visited and grid[r - 1][c] == "1": q.append((r - 1, c))
                        if 0 <= c + 1 < cols and (r, c + 1) not in visited and grid[r][c + 1] == "1": q.append((r, c + 1))
                        if 0 <= c - 1 < cols and (r, c - 1) not in visited and grid[r][c - 1] == "1": q.append((r, c - 1))

        return islands