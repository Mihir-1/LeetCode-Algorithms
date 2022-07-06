class Solution(object):
    def longestConsecutive(self, nums):
        maxSeq = 0;
        numSet = set()
        for n in nums:
            numSet.add(n)
        for n in nums:
            curSeq = 1;
            if n - 1 not in numSet:
                while n + 1 in numSet:
                    curSeq += 1
                    n += 1
            maxSeq = max(curSeq, maxSeq)
        return maxSeq
            
        