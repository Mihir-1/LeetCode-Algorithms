class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        res = (r - l) * min(height[l], height[r])
        while l < r:
            if height[l] < height[r]:
                l += 1
                res = max(res, (r - l) * min(height[l], height[r]))
            else:
                r -= 1
                res = max(res, (r - l) * min(height[l], height[r]))
        return res