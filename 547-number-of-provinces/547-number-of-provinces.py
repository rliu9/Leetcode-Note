class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        def dfs(node):
            for nei, connected in enumerate(isConnected[node]):
                if connected and nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        res = 0
        for city in range(len(isConnected)):
            if city not in seen:
                dfs(city)
                res += 1
        return res