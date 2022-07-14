class Solution(object):
    def isValid(self, s):
        stack = []
        parens = {"(" : ")", "{" : "}", "[" : "]"}
        for c in s:
            if c in parens.keys():
                stack.append(c)
            elif stack and c == parens.get(stack[-1], ""):
                stack.pop()
            else:
                return False
        return True if len(stack) == 0 else False
        