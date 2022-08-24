class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ifPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:return False
                l, r = l+1, r-1
            return True
        
        res = []
        def backtracking(s, start_index, cur):
            if start_index >= len(s):
                res.append(cur)
                return
            for i in range(start_index, len(s)):
                if ifPalindrome(s, start_index, i):
                    backtracking(s, i+1, cur+[s[start_index:i+1]])
        backtracking(s, 0, [])
        return res