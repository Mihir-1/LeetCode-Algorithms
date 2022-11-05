class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Initializes Keypad Map
        digLet = dict()
        j = 97
        for i in range(2, 10):
            letters = []
            for _ in range(3):
                letters.append(chr(j))
                j += 1
            if i == 7 or i == 9:
                letters.append(chr(j))
                j += 1
            digLet[i] = letters
            
        # Algorithm
        res = []
        def dfs(i, cur):
            # Base Case: reached end of string
            if i == len(digits):
                res.append(cur)
                return
            # Call dfs with each option
            for letter in digLet[int(digits[i])]:
                dfs(i + 1, cur + letter)
        
        dfs(0, '')
        return res if len(digits) > 0 else []
    
    """
    ASSUMING: digits.length is not constant
    Runtime: 2^n
              - 4^n (Each index in input has up to 4 branches: foreach letter)
    Memory:  2^n 
              - 2^n (Length of res) 
              > 
              Ignored:
              - n/2 Recursive Stack Length
    """
        