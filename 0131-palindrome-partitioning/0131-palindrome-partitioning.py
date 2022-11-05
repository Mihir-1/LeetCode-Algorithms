class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(cur, i):
            # Valid Palindrome
            valid = cur[-1] == cur[-1][::-1]

            # Base Case if i = len(s)
            if i == len(s):
                if valid:
                    res.append(cur)
                return
            
            # If Valid pal: append to cur -> dfs
            if valid:
                dfs(cur + [s[i]], i + 1)
            
            # Append to cur[-1] -> dfs
            dfs(cur[:-1] + [cur[-1] + s[i]], i + 1)
            return
            
        dfs([s[0]], 1)
        return res
    
    """
    ASSUMING: s.length is not constant
    Runtime: 2^n
              - 2^n (Each index in input has 2 branches: include not include)
    Memory:  2^n 
              - 2^n (Length of res) 
              > 
              Ignored:
              - n/2 Recursive Stack Length
    """