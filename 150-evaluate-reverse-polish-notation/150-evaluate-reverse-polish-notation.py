class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+" or t == "-" or t == "*" or t == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    stack.append(int(a / b))
            else:
                stack.append(t)
        return stack[-1]