class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        partitions = [0]
        nums = set()
        for i, num in enumerate(arr):
            nums.add(num)
            #print(nums, set([val for val in range(partitions[-1], i + 1)]))
            if nums == set([val for val in range(partitions[-1], i + 1)]):
                nums = set()
                partitions.append(i + 1)
        return len(partitions) - 1
            