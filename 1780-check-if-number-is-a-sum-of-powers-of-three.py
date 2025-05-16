class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # Base 3 check
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True
        '''
        Time: O(log3n)
        Space: O(1)
        '''

        """
        # Precompute powers
        power = [1] # power[i] = 3^i
        while power[-1] <= n:
            power.append(3 * power[-1])
        
        for i in range(len(power) - 1, -1, -1):
            if power[i] <= n:
                n -= power[i]
        
        return n == 0

        '''
        Time: O(log3n)
        Space: O(log3n) 
        '''
        """
