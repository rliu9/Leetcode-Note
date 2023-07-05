class Solution:
    def longestWord(self, words: List[str]) -> str:
        l = set([])
        words.sort(key=len)
        for word in words:
            if len(word) == 1 or word[:-1] in l:
                l.add(word)
        return max(sorted(l), key=len) if l else ""