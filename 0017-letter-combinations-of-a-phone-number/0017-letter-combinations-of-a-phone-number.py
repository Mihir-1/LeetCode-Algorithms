class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Initializes Keypad Map
        phone = dict()
        j = 97
        for i in range(2, 10):
            letters = []
            for _ in range(3):
                letters.append(chr(j))
                j += 1
            if i == 7 or i == 9:
                letters.append(chr(j))
                j += 1
            phone[i] = letters
        
        res = []
        def dfs(i, cur):
            print(cur)
            # Base Case: reached end of string
            if i == len(digits):
                res.append(cur)
                return
            # Call dfs with each option
            for letter in phone[int(digits[i])]:
                dfs(i + 1, cur + letter)
        
        dfs(0, '')
        return res if len(digits) > 0 else []