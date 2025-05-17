class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Frequency
        freq = [0] * (max(nums) + 1)
        for num in nums:
            freq[num] += 1
        
        res = left = cur = 0
        for right in range(len(freq)):
            # Shrink window 
            if left < right - 2 * k:
                cur -= freq[left]
                left += 1
            cur += freq[right]
            res = max(cur, res)
        
        return res
        '''
        Time: O(n)
        Space: O(n)
        '''
        
        """
        # Sort
        nums.sort()
        res = start = 0
        for end in range(len(nums)):
            while nums[end] - nums[start] > 2 * k:
                start += 1
            res = max(end - start + 1, res)
            
        return res
        '''
        Time: O(n logn)
        Space: O(1)
        '''
        """
