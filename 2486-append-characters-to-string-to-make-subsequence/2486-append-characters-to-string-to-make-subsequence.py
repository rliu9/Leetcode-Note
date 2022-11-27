class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        while i < len(s) and j < len(t):
            j += (s[i]==t[j])
            i += 1
        return len(t)-j