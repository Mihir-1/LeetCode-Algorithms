class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_point = list(zip([(point[0] ** 2 + point[1] ** 2) ** (1/2) for point in points], points))
        heapify(dist_point)
        return [heappop(dist_point)[1] for _ in range(k)]