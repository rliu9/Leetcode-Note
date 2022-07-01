class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = defaultdict(int)
        for i in range(len(s)):
            l = []
            if i+10 <= len(s):
                l.append(s[i:i+10])
            d["".join(l)] += 1
        res = []
        for key, value in d.items():
            if key and value > 1:
                res.append(key)
        return res