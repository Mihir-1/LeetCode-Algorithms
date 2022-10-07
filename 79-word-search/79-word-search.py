class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, word, used):
            if len(word) == 0:
                return True
            if (0 > i or i >= len(board)) or (0 > j or j >= len(board[0])) or word[0] != board[i][j] or (i, j) in used:
                return False
            # print("Current:", board[i][j])
            # print("word:", word)
            # print("used", used)
            
            possible = False

            used.add((i, j))
            newWrd = word[1:]
            possible = dfs(i + 1, j, newWrd, used) or dfs(i - 1, j, newWrd, used) or dfs(i, j + 1, newWrd, used) or dfs(i, j - 1, newWrd, used)
            used.remove((i, j))
            return possible
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, word, set()):
                        return True
        return False
    
    

    
