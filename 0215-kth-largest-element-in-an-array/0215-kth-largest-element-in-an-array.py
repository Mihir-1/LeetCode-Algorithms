class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            if len(minHeap) == k:
                heappushpop(minHeap, num)
            else:
                heappush(minHeap, num)
        return minHeap[0]