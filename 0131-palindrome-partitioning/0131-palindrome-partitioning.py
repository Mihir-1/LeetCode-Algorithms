class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(cur, i):
            valid = cur[-1] == cur[-1][::-1]
            #print(cur, i, valid)
            # If Valid pal: append to cur -> dfs
            if i == len(s):
                if valid:
                    res.append(cur)
                return
            if valid:
                # Base Case if i = len(s)
                dfs(cur + [s[i]], i + 1)
            # Append to cur[-1] -> dfs
            dfs(cur[:-1] + [cur[-1] + s[i]], i + 1)
            
        dfs([s[0]], 1)
        return res