class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:return True
        idx = 0
        for i,n in enumerate(t):
            if n == s[idx]:
                if idx == len(s)-1:return True
                idx += 1
        return False