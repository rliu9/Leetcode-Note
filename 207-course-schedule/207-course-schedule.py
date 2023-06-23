class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        visited = set()
        for c, pre in prerequisites:
            preMap[c].append(pre)
        def dfs(c):
            if c in visited:return False
            if not preMap[c]:return True
            visited.add(c)
            for i in preMap[c]:
                if not dfs(i):return False
            visited.remove(c)
            preMap[c] = []
            return True
        for c in range(numCourses):
            if not dfs(c):return False
        return True
    
    # O(V+E)
    # V: the number of courses
    # E: the number of dependencies