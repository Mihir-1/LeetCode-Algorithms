class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Get Frequencies
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        good = 0
        for num, count in counts.items():
            good += (count**2 - count) / 2
        return int(good)
'''
    Number of good pairs for n numbers:
        1: 0 
        2: 1 ---> 1
        3: 3 ---> 2
        4: 6 ---> 3
        5: 10 ---> 4
        
        y =  0.5 * x^2 - 0.5x
        y = 0.5(x**2 - x)
''' 
