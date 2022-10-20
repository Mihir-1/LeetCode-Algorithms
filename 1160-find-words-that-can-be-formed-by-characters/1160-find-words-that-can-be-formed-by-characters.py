class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = dict()
        
        for c in chars:
            charFreq = freq.get(c, 0) + 1
            freq[c] = charFreq
        
        lengths = 0
        for word in words:
            temp = dict()
            for i, item in enumerate(freq.items()):
                temp[item[0]] = item[1]
            validWord = True
            for c in word:
                count = temp.get(c, 0)
                if count == 0:
                    validWord = False
                    break
                else:
                    count -= 1
                temp[c] = count
            if validWord:
                lengths += len(word)
        
        return lengths