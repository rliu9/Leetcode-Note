class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for a,b in zip(s, t):
            if a not in d1 and b not in d2:
                d1[a] = b
                d2[b] = a
            elif d1.get(a) != b and d2.get(b) != a:
                return False
        return True
    
    # O(n)
    # O(n)