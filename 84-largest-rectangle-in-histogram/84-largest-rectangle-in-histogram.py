class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # tuple: (int: (start idx), int: (height))
        a = 0
        
        for i, h in enumerate(heights):
            val = [i]
            while stack and stack[-1][1] > h:
                val = stack.pop()
                a = max(a, (i - val[0]) * val[1])
            stack.append((val[0], h))
        
        for i, h in stack:
            a = max(a, (len(heights) - i) * h)
            
        return a