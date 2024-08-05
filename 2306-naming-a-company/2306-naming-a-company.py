class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # Initialize & Populate dictionary mapping prefix to suffix for each word
        prefixToSuffix = dict()
        for idea in ideas:
            suffixes = prefixToSuffix.get(idea[0], set())
            suffixes.add(idea[1:])
            prefixToSuffix[idea[0]] = suffixes

        # Iterate over all prefix combinations and add valid pairs to total
        ideaCount = 0
        prefixes = list(prefixToSuffix.keys())
        for i in range(len(prefixes)):
            for j in range(i + 1, len(prefixes)):
                p1, p2 = prefixes[i], prefixes[j]
                s1, s2 = prefixToSuffix[p1], prefixToSuffix[p2]
                intersection = len(s1 & s2)
                ideaCount += (len(s1) - intersection) * (len(s2) - intersection)

        return 2 * ideaCount