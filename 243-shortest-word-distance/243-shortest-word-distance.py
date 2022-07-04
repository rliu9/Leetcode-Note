class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx1,idx2, = [],[]
        for i,word in enumerate(wordsDict):
            if word1 == word:
                idx1.append(i)
            if word2 == word:
                idx2.append(i)
        return min(abs(i-j) for i in idx1 for j in idx2)