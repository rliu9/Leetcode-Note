class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter, n = collections.Counter(s1), len(s1)
        for i in range(len(s2)):
            if counter == collections.Counter(s2[i:i+n]):return True
        return False