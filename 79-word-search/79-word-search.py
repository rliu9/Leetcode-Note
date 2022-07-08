class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col = len(board),len(board[0])
        def backtracking(r,c,idx):
            if idx >= len(word):
                return True
            if r >= row or c >= col or c < 0 or r < 0 or word[idx]!=board[r][c]:
                return False
            value = board[r][c]
            board[r][c] = '#'
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                if backtracking(r+dx,c+dy,idx+1):
                    return True
            board[r][c] = value
            return False
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and backtracking(i,j,0):
                    return True
        return False
    
    # time complexity: O(N 3^L); N:# of cells in the board; L:length of the word
    # space Complexity: O(L)
    
if __name__ == '__main__':
    assert True == Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")