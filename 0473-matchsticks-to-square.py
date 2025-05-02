class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        
        sideLength = sum(matchsticks) / 4
        
        lengths = [0] * 4
        matchsticks.sort(reverse = True)
        
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for side in range(4):
                if lengths[side] + matchsticks[i] <= sideLength:
                    lengths[side] += matchsticks[i]
                    if backtrack(i + 1):
                        return True

                    lengths[side] -= matchsticks[i]
        
            return False

        return backtrack(0)

'''
Time: O(4^n)
Space: O(n)
'''
