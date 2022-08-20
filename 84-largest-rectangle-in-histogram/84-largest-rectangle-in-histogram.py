class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # tuple: (int: (start idx), int: (height))
        maxArea = 0
        
        # Iterate array
        for i, height in enumerate(heights):
            val = [i]
            while stack and stack[-1][1] > height:
                val = stack.pop()
                area = (i - val[0]) * val[1]
                maxArea = max(maxArea, area)
            stack.append((val[0], height))
        
        # Empty stack
        while stack:
            val = stack.pop()
            area = (len(heights) - val[0]) * val[1]
            maxArea = max(maxArea, area)
            
        return maxArea