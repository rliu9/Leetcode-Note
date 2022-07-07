class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strings:
            keys = []
            for i,n in enumerate(s):
                if i>=1:
                    keys.append(chr((ord(n)-ord(s[i-1])) % 26 + ord('a')))
            key = ''.join(keys)
            d[key].append(s)
        return [i for i in d.values()]