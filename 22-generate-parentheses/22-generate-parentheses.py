class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(l, r, cur):
            if len(cur) == n*2:
                res.append(''.join(cur))
            if l < n:
                backtracking(l+1, r, cur+['('])
            if r < l:
                backtracking(l, r+1, cur+[')'])
        backtracking(0, 0, [])
        return res
        
            