class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            if ((m + 1 < n and nums[m] == nums[m + 1] and not m % 2) or 
                (m - 1 >= 0 and nums[m] == nums[m - 1] and m % 2)):
                l = m + 1
            elif ((m + 1 < n and nums[m] == nums[m + 1] and m % 2) or
                (m - 1 >= 0 and nums[m] == nums[m - 1]) and not m % 2):
                r = m
            else:
                return nums[m]
        return -1
        
        
        '''
        Time: O(log n)
        Space: O(1)

        binary search condition
        even idx, same element before -> single comes before
        odd idx, same element after -> single comes before

        even idx, same element after -> single comes after 
        odd idx, same element before -> single comes after 

        same element neither before nor after -> return

        Edge Case:
        cant check element before/after out of bounds
        '''
