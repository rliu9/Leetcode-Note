class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        d = dict(sorted(c.items(), key=lambda x:x[1]))
        dd = collections.defaultdict(list)
        for key,value in d.items():
            dd[value].append(key)
        
        dd = dict(sorted(dd.items(), key=lambda x:-x[0]))
        res = []
        for i in range(k):
            for k in dd:
                value = min(dd[k])
                res.append(value)
                dd[k].remove(value)
                if not dd[k]:del dd[k]
                break
        return res