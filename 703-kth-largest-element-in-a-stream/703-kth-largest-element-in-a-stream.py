class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.maxHeap = nums
#         heapify(self.maxHeap)
#         self.k = k

#     def add(self, val: int) -> int:
#         heappush(self.maxHeap, val)
#         return nlargest(self.k, self.maxHeap)[-1]
    def __init__(self, k: int, nums: List[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)