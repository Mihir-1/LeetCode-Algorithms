class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l: List[int], r: List[int]) -> List[int]:
            # print('left', l,'\nright', r, '\n')
            if len(l) == 1 and len(r) == 1:
                return l + r if l[0] < r[0] else r + l
            if len(l) == 0:
                return r
            if len(r) == 0:
                return l
            l = merge(l[:len(l) // 2], l[len(l) // 2:])
            r = merge(r[:len(r) // 2], r[len(r) // 2:])
            # print('merging', l,'\n', r)
            i, j = 0, 0
            merged = []
            while i < len(l) or j < len(r):
                if i == len(l): 
                    merged.append(r[j])
                    j += 1
                else: 
                    if j == len(r) or l[i] <= r[j]:
                        merged.append(l[i])
                        i += 1
                    else:
                        merged.append(r[j])
                        j += 1
            # print('merged', merged)
            return merged
              
        return merge(nums[:len(nums) // 2], nums[len(nums) // 2:])