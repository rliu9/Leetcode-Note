class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            d[key].append(s)
        res = []
        for key,value in d.items():
            res.append(value)
        return res