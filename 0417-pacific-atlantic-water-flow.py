class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]

        def dfs(r, c, ocean, prev):
            if r < 0 or c < 0 or r > rows - 1 or c > cols - 1 or ocean[r][c] or heights[r][c] < prev:
                return
            
            ocean[r][c] = True
            curHeight = heights[r][c]
            dfs(r + 1, c, ocean, curHeight)
            dfs(r - 1, c, ocean, curHeight)
            dfs(r, c + 1, ocean, curHeight)
            dfs(r, c - 1, ocean, curHeight)

        for r in range(rows):
            dfs(r, 0, pac, 0)
            dfs(r, cols - 1, atl, 0)
        
        for c in range(cols):
            dfs(0, c, pac, 0)
            dfs(rows - 1, c, atl, 0)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res
        '''
        Time: O(m * n)
        Space: O(m * n)
        '''
