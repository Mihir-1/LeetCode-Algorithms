class Solution(object):
    def maxArea(self, height):
        l = 0
        h = len(height) - 1
        m = min(height[l], height[h]) * (h - l)
        while (h - l > 1):
            temp = l
            if height[l] <= height[h]:
                while height[temp] > height[temp + 1]:
                    temp += 1
                temp += 1
            if height[h] <= height[l]:
                while height[h] > height[h - 1]:
                    h -= 1
                h -= 1
            l = temp
            if (min(height[l], height[h]) * (h - l) > m):
                m = min(height[l], height[h]) * (h - l)
        return m