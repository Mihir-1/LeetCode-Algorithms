class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Optimal
        unique_nums = len(set(nums))
        num_freq = dict()
        total = 0

        left = 0
        right = 0

        while left < len(nums):
            # Incomplete: Increment right
            while right < len(nums) and len(num_freq) < unique_nums:
                num_freq[nums[right]] = 1 + num_freq.get(nums[right], 0)
                right += 1

            # If complete, add to total
            if len(num_freq) == unique_nums:
                total += 1 + (len(nums) - right)

            # Update freq, increment left
            num_freq[nums[left]] -= 1
            if num_freq[nums[left]] == 0:
                num_freq.pop(nums[left])

            left += 1
            
        return total


        '''
        Time: O(n)
        Space: O(n)
        '''

        '''
        # Brute Force

        unique_nums = len(set(nums))
        total = 0

        for i in range(len(nums)):
            cur_uniques = set()
            for j in range(i + 1, len(nums) + 1):
                cur_uniques.add(nums[j - 1])
                if len(cur_uniques) == unique_nums:
                    total += 1

        return total
        
        Time: O(n^2)
        Space: O(n)

        '''
