class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0
        
        for r in range(rows):
            for c in range(cols):
                # BFS
                q = deque()
                area = 0
                if bool(grid[r][c]) and (r, c) not in visited:
                    q.append((r, c))
                while q: 
                    #print('\t', q)
                    row, col = q.popleft()
                    if (row, col) not in visited:
                        visited.add((row, col))
                        area += 1
                        if 0 <= row + 1 < rows and (row + 1, col) not in visited and bool(grid[row + 1][col]): q.append((row + 1, col))
                        if 0 <= row - 1 < rows and (row - 1, col) not in visited and bool(grid[row - 1][col]): q.append((row - 1, col))
                        if 0 <= col + 1 < cols and (row, col + 1) not in visited and bool(grid[row][col + 1]): q.append((row, col + 1))
                        if 0 <= col - 1 < cols and (row, col - 1) not in visited and bool(grid[row][col - 1]): q.append((row, col - 1))
                res = max(area, res)
                #print(r, c, area)
        return res
    