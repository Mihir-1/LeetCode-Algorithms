class Solution:
    def removeStars(self, s: str) -> str:
        # Initialize stack
        stack = []

        # Remove stars
        for c in s:
            if c == '*' and stack: 
                stack.pop()
            else: 
                stack.append(c)

        # Return stringified
        return ('').join(stack)
