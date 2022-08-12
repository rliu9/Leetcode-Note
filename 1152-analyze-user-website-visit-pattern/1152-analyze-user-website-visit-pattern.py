import itertools
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        d = collections.defaultdict(list)
        for i in sorted(zip(username, timestamp, website), key=lambda k:(k[0],k[1])):
            d[i[0]].append(i[2])
        d_combination = collections.defaultdict(list)
        for i in d:
            comb = set(itertools.combinations(d[i],3))
            if comb:
                d_combination[i] = comb
        
        list_pattern = [value for sub in d_combination.values() for value in sub]
        d_pattern = dict(Counter(list_pattern))
        return max(sorted(d_pattern), key=d_pattern.get)