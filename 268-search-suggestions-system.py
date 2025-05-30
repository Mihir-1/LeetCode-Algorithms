class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        start, end = 0, len(products) - 1

        for i, c in enumerate(searchWord):
            # Find Start of window
            l, r = start, end
            while l < r:
                m = (l + r) // 2
                if len(products[m]) - 1 < i or products[m][i] < c:
                    l = m + 1
                elif products[m][i] >= c:
                    r = m
            start = l

            if len(products[start]) - 1 < i or products[start][i] != c:
                for j in range(i, len(searchWord)):
                    res.append([])
                break

            # Find End of window
            l, r = start, end
            while l < r:
                m = (1 + l + r) // 2
                if len(products[m]) - 1 < i or products[m][i] <= c:
                    l = m
                else:
                    r = m - 1
            end = l
            terms = []
            for j in range(min(3, end + 1 - start)):
                terms.append(products[start + j])
            res.append(terms)
        return res

'''
Time: O(nlogn)
Space: O(1)
'''



