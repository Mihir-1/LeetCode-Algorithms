class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Initialize gaps dictionary
        gaps = {0 : 0}
        
        for layer in wall:
            total = 0
            for num in layer[:-1]:
                total += num
                gaps[total] = 1 + gaps.get(total, 0)

        return len(wall) - max(gaps.values())