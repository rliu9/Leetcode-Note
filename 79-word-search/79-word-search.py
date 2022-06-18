class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col,n = len(board),len(board[0]),len(word)
        def backtracking(r,c,idx):
            if idx == n:
                return True
            if r < 0 or c < 0 or r == row or c == col:
                return False
            if board[r][c] != word[idx]:
                return False
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                rr,cc = r+dr,c+dc
                value = board[r][c]
                board[r][c] = '.'
                if backtracking(rr,cc,idx+1):
                    return True
                board[r][c] = value
            
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if backtracking(i,j,0):
                        return True

        return False
    
    # time complexity: O(N 3^L); N:# of cells in the board; L:length of the word
    # space Complexity: O(L)
    
if __name__ == '__main__':
    assert True == Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")