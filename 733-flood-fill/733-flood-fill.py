class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        seen,row,col,color = set(), len(image),len(image[0]),image[sr][sc]
        if color == newColor:return image
        def dfs(r,c,image,newColor):
            if 0 <= r < row and 0 <= c < col:
                if image[r][c] == color:
                    image[r][c] = newColor
                    dfs(r-1,c,image,newColor)
                    dfs(r+1,c,image,newColor)
                    dfs(r,c-1,image,newColor)
                    dfs(r,c+1,image,newColor)
        dfs(sr,sc,image,newColor)
        return image