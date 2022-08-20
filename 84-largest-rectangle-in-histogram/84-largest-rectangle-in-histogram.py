class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # tuple: (int: (start idx), int: (height))
        maxArea = 0
        
        # Iterate array
        for i, h in enumerate(heights):
            val = [i]
            while stack and stack[-1][1] > h:
                val = stack.pop()
                maxArea = max(maxArea, (i - val[0]) * val[1])
            stack.append((val[0], h))
        
        # Empty stack
        while stack:
            val = stack.pop()
            maxArea = max(maxArea, (len(heights) - val[0]) * val[1])
            
        return maxArea