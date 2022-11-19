class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = collections.defaultdict(list)
        visit = set()
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        def dfs(crs):
            if crs in visit:return False
            if preMap[crs] == []:return True
            visit.add(crs)
            for c in preMap[crs]:
                if not dfs(c):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):return False
        return True