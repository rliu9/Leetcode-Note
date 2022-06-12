class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = collections.Counter(p)
        cur = collections.Counter()
        n,m,res = len(s),len(p)-1,[]
        for i in range(n):
            cur[s[i]] += 1
            if i>=m:
                if cur == counter:
                    res.append(i-m)
                if cur[s[i-m]] > 1:
                    cur[s[i-m]] -= 1
                else:
                    del cur[s[i-m]]   
        return res
    
    # time complexity: O(n)
    # space complexity: O(M+N)
    