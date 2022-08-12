class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        combined_info=collections.defaultdict(list)
        for item in sorted(zip(username, timestamp, website), key = lambda k:(k[0],k[1])):
            combined_info[item[0]].append(item[2])
            
        patern_dict = {}
        for key in combined_info.keys():
            patern = set(combinations(combined_info[key],3))
            if patern:
                patern_dict[key]=patern
        paternScore_dict = dict(Counter([d2 for d in patern_dict.values() for d2 in d]))
        
        return sorted(paternScore_dict, key = lambda k:(-paternScore_dict[k],k))[0]