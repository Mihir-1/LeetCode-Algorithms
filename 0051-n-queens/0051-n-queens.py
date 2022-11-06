class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Queens State Variables
        board = [['.'] * n for _ in range(n)]
        rcdiff = set()
        rcsum = set()
        cols = set()
        res = []
        
        def dfs(r):
            # Base Case: end of board
            if r == n:
                res.append([''.join(board[i]) for i in range(n)])
                return
            for c in range(n):
                #print(r, c)
                if (r - c not in rcdiff) and (r + c not in rcsum) and (c not in cols):
                    board[r][c] = 'Q'
                    rcdiff.add(r - c)
                    rcsum.add(r + c)
                    cols.add(c)
                    dfs(r + 1)
                    rcdiff.remove(r - c)
                    rcsum.remove(r + c)
                    cols.remove(c)
                    board[r][c] = '.'
                    
            
        dfs(0)
        return res