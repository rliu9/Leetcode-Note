class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s) == Counter(t)
        char = {}
        for i in s:
            if i not in char:
                char[i] = 1
            else:
                char[i] += 1
        for j in t:
            if j not in char:
                return False
            char[j] -= 1
        for c in char:
            if char[c] != 0:return False
        return True
    
    # O(n)
    # O(1)
    