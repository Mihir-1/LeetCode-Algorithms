class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacleSet = {(x, y) for x, y in obstacles}
        maxDistance = 0
        position = [0, 0]
        d = 0 # North
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for com in commands:
            if com == -2:
                d = (d - 1) % 4
            elif com == -1:
                d = (d + 1) % 4
            else:
                for _ in range(com):
                    nextPos = [position[0] + directions[d][0], position[1] + directions[d][1]]
                    if tuple(nextPos) in obstacleSet:
                        break
                    position = nextPos
                maxDistance = max(position[0] ** 2 + position[1] ** 2, maxDistance)

        return maxDistance
    '''
    Time: O(S) - Total steps: (Sum of commands)
    Space: O(O) - Obstacles
    '''
