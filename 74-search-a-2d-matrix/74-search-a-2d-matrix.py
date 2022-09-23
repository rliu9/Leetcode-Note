class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx, l, r = 0, 0, len(matrix[0])-1
        for n in (zip(*matrix)):
            for m in n:
                if m>target:break
                idx += 1
            break
        if idx>0:idx-=1
        while l <= r:
            mid = (l+r)//2
            if matrix[idx][mid] == target:return True
            if matrix[idx][mid] < target:l=mid+1
            else:r=mid-1
        return False
            