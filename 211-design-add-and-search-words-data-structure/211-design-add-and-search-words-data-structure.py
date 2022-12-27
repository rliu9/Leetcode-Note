class WordDictionary:

    def __init__(self):
        self.d = collections.defaultdict(list)

    def addWord(self, word: str) -> None:
        self.d[len(word)].append(word)

    def search(self, word: str) -> bool:
        if not self.d[len(word)]:return False
        positions = []
        for i,n in enumerate(word):
            if n != '.':positions.append(i)
        if not positions:return True
        for w in self.d[len(word)]:
            for i in positions:
                if word[i] != w[i]:break
                if i == positions[-1]:return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)