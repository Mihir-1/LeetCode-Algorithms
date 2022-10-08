class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapify(stones)
        while len(stones) > 1:
            a = heappop(stones)
            b = heappop(stones)
            if b - a:
                heappush(stones, a - b)
        return -1 * stones[0] if stones else 0