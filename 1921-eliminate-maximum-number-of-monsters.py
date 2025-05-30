class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        timeToReach = [math.ceil(d / s) for d, s in zip(dist, speed)]
        timeToReach.sort()

        elims = 0
        for t, monsterTime in enumerate(timeToReach):
            if t >= monsterTime:
                return elims
            elims += 1

        return elims
        
        '''
        Time: O(n)
        Space: O(n)
        '''
