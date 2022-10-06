class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [None] * 26

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.end = True

    def search(self, word: str) -> bool:
        #print("word: ", word, "\n")
        def dfs(w, node):
            #print(w)
            if not node:
                return False
            if len(w) == 0:
                return node.end
            if w[0] == ".":
                for child in node.children:
                    #print(chr(i + ord('a')))
                    if child and dfs(w[1:], child):
                        return True
            else:
                node = node.children[ord(w[0]) - ord("a")]
                if not node:
                    return False
                return dfs(w[1:], node)
        return dfs(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)