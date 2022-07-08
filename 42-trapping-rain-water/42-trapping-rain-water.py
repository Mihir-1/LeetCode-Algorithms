class Solution(object):
    def trap(self, height):
        area = 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                #if height[l] < maxL:
                area += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                #if height[r] < maxR:
                area += maxR - height[r]
        return area
        