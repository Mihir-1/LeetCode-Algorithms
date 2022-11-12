class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) 
        q = deque()
        visited = set()

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: q.append((r, c))
        
        iters = -1
        if not q: iters += 1 
        
        while q:
            print(q)
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                grid[r][c] = 2
                if 0 <= r + 1 < rows and grid[r + 1][c] == 1 and (r + 1, c) not in visited: 
                    visited.add((r + 1, c))
                    q.append((r + 1, c))
                if 0 <= r - 1 < rows and grid[r - 1][c] == 1 and (r - 1, c) not in visited:
                    visited.add((r - 1, c))
                    q.append((r - 1, c))
                if 0 <= c + 1 < cols and grid[r][c + 1] == 1 and (r, c + 1) not in visited: 
                    visited.add((r, c + 1))
                    q.append((r, c + 1))
                if 0 <= c - 1 < cols and grid[r][c - 1] == 1 and (r, c - 1) not in visited: 
                    visited.add((r, c - 1))
                    q.append((r, c - 1))
            iters += 1
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: return -1
        return iters 