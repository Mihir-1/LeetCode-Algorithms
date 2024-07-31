class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        # Build map of cities {from : to}
        pathDict = {}
        for from_, to_ in paths:
            pathDict[from_] = to_
        
        # Iterate until key does not exist (destination only city)
        cur = paths[0][1]
        while cur in pathDict:
            cur = pathDict[cur]
        
        return cur