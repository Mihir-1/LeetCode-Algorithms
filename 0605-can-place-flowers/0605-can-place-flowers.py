class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if (i < len(flowerbed) - 1 and flowerbed[i + 1] == 0) or i == len(flowerbed) - 1:
                if (flowerbed[i - 1] == 0 and flowerbed[i] == 0) or (i == 0 and flowerbed[i] == 0):
                    if n == 1: return True
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0
            