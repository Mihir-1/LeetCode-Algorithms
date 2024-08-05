import heapq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings

        self.foodIdxMap = dict()
        for i, food in enumerate(foods):
            self.foodIdxMap[food] = i
        
        self.highestRatedMap = dict()
        for i, cuisine in enumerate(cuisines):
            heap = self.highestRatedMap.get(cuisine, [])
            heappush(heap, (-1 * ratings[i], self.foods[i]))
            self.highestRatedMap[cuisine] = heap

    def changeRating(self, food: str, newRating: int) -> None:
        idx = self.foodIdxMap[food]
        cuisine = self.cuisines[idx]
        self.ratings[idx] = newRating
        heap = self.highestRatedMap.get(cuisine)
        heappush(heap, (-1 * newRating, self.foods[idx]))
        return

    def highestRated(self, cuisine: str) -> str:
        heap = self.highestRatedMap.get(cuisine)
        rating, food = heappop(heap)
        rating *= -1
        while self.ratings[self.foodIdxMap[food]] != rating and heap:
            rating, food = heappop(heap)
            rating *= -1
        heappush(heap, (-1 * rating, food))
        return food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)