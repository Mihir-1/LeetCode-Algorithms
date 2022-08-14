class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = list(zip(position, speed))
        ps.sort(reverse = True)
        stack = []
        for pos, speed in ps:
            if not stack or (target - pos) / speed > (target - stack[-1][0]) / stack[-1][1]:
                stack.append((pos, speed)) 
        return len(stack)