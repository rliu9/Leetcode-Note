class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcounter = collections.Counter(p)
        n = len(p)
        res = []
        for i in range(n, len(s)+1):
            c = collections.Counter(s[i-n:i])
            if c == pcounter:res.append(i-n)
        return res