class Solution(object):
    def hammingWeight(self, n):
        count = 0
        for i in range (0, 32):
            print(bin(n)[-1])
            if bin(n)[-1] == '1':
                count += 1
            n = n >> 1
        return count
            