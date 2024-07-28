class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Initialize gaps dictionary {position : number of gaps}
        gaps = {0 : 0}
        
        # Populate dictionary
        for layer in wall:
            total = 0
            for num in layer[:-1]:
                total += num
                gaps[total] = 1 + gaps.get(total, 0)
        
        # Return wall height minus greatest number of gaps -> number of bricks needed to be broken
        return len(wall) - max(gaps.values())