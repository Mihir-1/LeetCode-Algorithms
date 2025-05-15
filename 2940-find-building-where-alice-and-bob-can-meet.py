import math

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # Binary lifting solution
        n = len(heights)
        stack = [] # Monotonic decreasing stack 
        nextLarger = [-1] * n

        for i in range(n - 1, -1, -1):
            while stack and heights[i] >= heights[stack[-1]]:
                stack.pop()
            if stack:
                nextLarger[i] = stack[-1]
            stack.append(i)
        
        # Preprocess jumps - binary lifting
        logn = math.ceil(math.log2(n))
        jump = [nextLarger.copy()]
        for i in range(logn):
            prev = jump[-1]
            cur = [-1] * n
            for j in range(n):
                if prev[j] != -1:
                    cur[j] = prev[prev[j]]
            jump.append(cur)

        res = []
        for a, b in queries:
            if a == b:
                res.append(a)
                continue
            # reorder s.t. b >= a
            if a > b:
                a, b = b, a

            if heights[b] > heights[a]: # a goes to b's building
                res.append(b)
            elif nextLarger[a] == -1: # No following taller building
                res.append(-1)
            else:
                i = b
                for k in range(logn - 1, -1, -1):
                    nxt = jump[k][i]
                    if nxt != -1 and heights[a] >= heights[nxt]:
                        i = nxt
                res.append(nextLarger[i])

        return res
        '''
        Time: O((n + q) * logn)
        Space: O(n * logn)
        '''
