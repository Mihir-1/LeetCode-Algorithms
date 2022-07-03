class Solution(object):
    def topKFrequent(self, nums, k):
        count = defaultdict(int)
        freq = [[] for n in nums]
        res = []
        for n in nums:
            count[n] += 1
        #print(count)
        for key, val in count.items():
            freq[val - 1].append(key)
            #print(freq)
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    return res
            