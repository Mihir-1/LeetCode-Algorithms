class Solution(object):
    def getSum(self, a, b):
        mask = 0xffffffff
        while (b & mask) > 0:
            temp = a ^ b
            b = (a & b) << 1
            a = temp
        if b > 0:
            return (a & mask)
        else:
            return a
