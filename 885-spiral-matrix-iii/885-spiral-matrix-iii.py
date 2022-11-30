class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        i, j = rStart, cStart
        left, right = cStart, cStart
        bottom, top = rStart, rStart
        result = [[i,j]]
        while top >= 0 or bottom < rows or left >= 0 or right < cols:
            j += 1 # step right into the next ring
            right += 1
            bottom += 1
            left -= 1
            top -= 1

            # go down
            while i < bottom:
                if 0 <= i and i < rows and 0 <= j and j < cols:
                    result.append([i,j])
                i += 1
            # go left
            while j > left:
                if 0 <= i and i < rows and 0 <= j and j < cols:
                    result.append([i,j])
                j -= 1
            # go up
            while i > top:
                if 0 <= i and i < rows and 0 <= j and j < cols:
                    result.append([i,j])
                i -= 1
            # go right
            while j < right:
                if 0 <= i and i < rows and 0 <= j and j < cols:
                    result.append([i,j])
                j += 1
            # if top-right of ring
            if 0 <= i and i < rows and 0 <= j and j < cols:
                result.append([i,j])
            
        return result