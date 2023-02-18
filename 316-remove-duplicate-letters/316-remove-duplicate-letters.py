class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = collections.Counter(s)
        idx = 0
        for i,n in enumerate(s):
            if n < s[idx]:
                idx = i
            c[n] -= 1
            if c[n] == 0:break
        return s[idx] + self.removeDuplicateLetters(s[idx:].replace(s[idx], '')) if s else ''