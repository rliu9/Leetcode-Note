class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.l = wordsDict
        self.d = collections.defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.d[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        w1, w2 = self.d[word1], self.d[word2]
        return min([abs(i-j) for i in w1 for j in w2])
        # O(mn) m,n - occurrences for two words


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)