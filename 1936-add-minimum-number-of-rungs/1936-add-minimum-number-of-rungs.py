class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        total = 0
        cur = 0
        for rung in rungs:
            total += ((rung - cur) - 1) // dist
            cur = rung
        return total