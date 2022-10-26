class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ifPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:return False
                l, r = l+1, r-1
            return True
        
        res = []
        def backtracking(s, idx, cur):
            if idx >= len(s):
                res.append(cur)
                return
            for i in range(idx, len(s)):
                if ifPalindrome(s, idx, i):
                    backtracking(s, i+1, cur+[s[idx:i+1]])
        backtracking(s, 0, [])
        return res
                    