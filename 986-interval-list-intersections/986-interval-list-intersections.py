class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        n,m = len(firstList),len(secondList)
        first = second = 0
        while first < n and second < m:
            i1,j1 = firstList[first]
            i2,j2 = secondList[second]
            i,j = max(i1,i2),min(j1,j2)
            if i<=j:res.append([i,j])
            if firstList[first][1] < secondList[second][1]:
                first += 1
            else:
                second += 1
        return res
    
    # time complexity: O(M+N)
    # space complexity: O(M+N)