class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def backtrack(cur, num):
            if len(cur) == k:
                res.append(cur.copy())
                return

            for i in range(num, n + 1):
                cur.append(i)
                backtrack(cur, i + 1) 
                cur.pop()           

        backtrack([], 1)
        return res 

        '''
        Time: O((k * n!) / (k! * (n - k)!))
        Res Space: O((k * n!) / (k! * (n - k)!))
        Auxillary Space: O(k)
        '''
