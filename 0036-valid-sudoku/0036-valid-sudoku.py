class Solution(object):
    def isValidSudoku(self, board):
        # check rows
        for i in range(0, 9):
            rowSet = set()
            for j in range(0, 9):
                if board[i][j] != ".":
                    if board[i][j] in rowSet:
                        return False
                    rowSet.add(board[i][j])
        # check columns
        for i in range(0, 9):
            colSet = set()
            for j in range(0, 9):
                if board[j][i] != ".":
                    if board[j][i] in colSet:
                        return False
                    colSet.add(board[j][i])
        # check squares
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                boxSet = set()
                for ii in range(0, 3):
                    for jj in range(0, 3):
                        if board[i + ii][j + jj] != ".":
                            if board[i + ii][j + jj] in boxSet:
                                return False
                            boxSet.add(board[i + ii][j + jj]) 
        return True