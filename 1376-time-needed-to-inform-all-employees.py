class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = dict()
        for i, mgr in enumerate(manager):
            subordinates[mgr] = [i] + subordinates.get(mgr, [])
        
        def dfs(mgr):
            if mgr not in subordinates:
                return 0
            
            maxTime = cur = informTime[mgr]
            for sub in subordinates[mgr]:
                maxTime = max(maxTime, cur + dfs(sub))

            return maxTime

        return dfs(headID)

'''
DFS: Find longest total informTime

Time: O(n)
Spcae: O(n)
'''
