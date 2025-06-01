class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # 1 pass 
        s = list(s)
        stack = [] # extraneous opens
        for i, c in enumerate(s):
            if c == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
            elif c == '(':
                stack.append(i)

        while stack:
            s[stack.pop()] = ''
        
        return ''.join(s)
        '''
        Time: O(n)
        Space: O(n)

        s = 5, 6
        )(())((
        maintain stack storing idx of opens - 
            if close 
                if stack empty, remove
                else pop                     
        remove opens from stack
        '''

        """
        # 2 pass
        removedCloses = []
        netOpens = 0

        for c in s:
            if c == ')':
                netOpens -= 1
                if netOpens < 0:
                    netOpens = 0
                    continue
            elif c == '(':
                netOpens += 1
            removedCloses.append(c)
        
        res = []
        for c in reversed(removedCloses):
            if c == '(' and netOpens > 0:
                netOpens -= 1
            else:
                res.append(c)
        
        return ''.join(reversed(res))
        
        '''
        Time: O(n)
        Space: O(n)
        1. iterate and remove all negative net opens (open - close < 0)
        2. iterate reverse and remove net opens (open - close > 0)
        '''
        """
