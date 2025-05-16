class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [char, count]
        
        # Build Stack
        for c in s:
            # 1. empty stack or c != top of stack -> append
            if not stack or c != stack[-1][0]:
                stack.append([c, 1])
            elif stack[-1][1] + 1 < k: # 2. count + 1 < k -> increment count
                stack[-1][1] += 1
            else: # 3. stack[-1][1] + 1 == k -> pop
                stack.pop()

        # Convert to String
        return ''.join(c * count for c, count in stack)

        '''
        Time: O(n)
        Space: O(n)
        '''
