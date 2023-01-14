
class Solution:
    def __init__(self):
        self.res = []
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.backtracking(0, 0, '', n)
        return self.res
    
    def backtracking(self, left, right, cur, n):
        if len(cur) == n*2:
            self.res.append(cur)
        if left < n:
            self.backtracking(left+1, right, cur+'(', n)
        if right < left:
            self.backtracking(left, right+1, cur+')', n)
        
            