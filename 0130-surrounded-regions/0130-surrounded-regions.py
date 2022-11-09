class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    # BFS
                    capture = True
                    island = set()
                    q = deque()
                    q.append((r, c))
                    # print(q)
                    while q:
                        row, col = q.popleft()
                        # print(row, col)
                        if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                            capture = False
                        island.add((row, col))
                        if 0 <= row + 1 < rows and board[row + 1][col] == 'O' and (row + 1, col) not in visited: 
                            q.append((row + 1, col))
                            visited.add((row + 1, col))
                        if 0 <= row - 1 < rows and board[row - 1][col] == 'O' and (row - 1, col) not in visited:
                            q.append((row - 1, col))
                            visited.add((row - 1, col))
                        if 0 <= col + 1 < cols and board[row][col + 1] == 'O' and (row, col + 1) not in visited:
                            q.append((row, col + 1))
                            visited.add((row, col + 1))
                        if 0 <= col - 1 < cols and board[row][col - 1] == 'O' and (row, col - 1) not in visited:
                            q.append((row, col - 1))
                            visited.add((row, col - 1))
                    #print(capture, island)
                    if capture:
                        for row, col in island:
                            board[row][col] = 'X'

        # # BFS
        # capture = True
        # island = set()
        # q = deque()
        # q.append((0, 1))
        # # print(q)
        # while q:
        #     row, col = q.popleft()
        #     # print(row, col)
        #     if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
        #         capture = False
        #     island.add((row, col))
        #     if 0 <= row + 1 < rows and board[row + 1][col] == 'O' and (row + 1, col) not in visited: 
        #         q.append((row + 1, col))
        #         visited.add((row + 1, col))
        #     if 0 <= row - 1 < rows and board[row - 1][col] == 'O' and (row - 1, col) not in visited:
        #         q.append((row - 1, col))
        #         visited.add((row - 1, col))
        #     if 0 <= col + 1 < cols and board[row][col + 1] == 'O' and (row, col + 1) not in visited:
        #         q.append((row, col + 1))
        #         visited.add((row, col + 1))
        #     if 0 <= col - 1 < cols and board[row][col - 1] == 'O' and (row, col - 1) not in visited:
        #         q.append((row, col - 1))
        #         visited.add((row, col + 1))

        # print(capture, island)

"""
Input:
[
["X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["O","X","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","X","X"],["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","X"],["O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O"],["O","O","O","O","O","X","O","O","O","O","X","O","O","O","O","O","X","O","O","X"],["X","O","O","O","X","O","O","O","O","O","X","O","X","O","X","O","X","O","X","O"],["O","O","O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O"],["X","O","O","O","X","X","X","O","X","O","O","O","O","X","X","O","X","O","O","O"],["O","O","O","O","O","X","X","X","X","O","O","O","O","X","O","O","X","O","O","O"],["X","O","O","O","O","X","O","O","O","O","O","O","X","X","O","O","X","O","O","X"],["O","O","O","O","O","O","O","O","O","O","X","O","O","X","O","O","O","X","O","X"],["O","O","O","O","X","O","X","O","O","X","X","O","O","O","O","O","X","O","O","O"],["X","X","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],["O","X","O","X","O","O","O","X","O","X","O","O","O","X","O","X","O","X","O","O"],["O","O","X","O","O","O","O","O","O","O","X","O","O","O","O","O","X","O","X","O"],["X","X","O","O","O","O","O","O","O","O","X","O","X","X","O","O","O","X","O","O"],["O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O","O"],["O","O","O","X","O","O","O","O","O","X","X","X","O","O","X","O","O","O","X","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["X","O","O","O","O","X","O","O","O","X","X","O","O","X","O","X","O","X","O","O"]]
"""