class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(l, r, s):
            if len(s) == n*2:
                res.append(''.join(s))
                return
            if l < n:
                s.append('(')
                backtracking(l+1, r, s)
                s.pop()
            if r < l:
                s.append(')')
                backtracking(l, r+1, s)
                s.pop()
        backtracking(0, 0, [])
        return res
            