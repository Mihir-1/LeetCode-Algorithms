class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        res = []
        
        def backtrack(l, r):
            if l == r == n:
                res.append("".join(stack))
                return
            
            if l < n:
                stack.append("(")
                backtrack(l + 1, r)
                stack.pop()
            
            if r < l:
                stack.append(")")
                backtrack(l, r + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res
        