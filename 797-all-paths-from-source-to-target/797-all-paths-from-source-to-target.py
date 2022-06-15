class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target,res = len(graph) - 1,[]

        def backtrack(currNode, path):
            if currNode == target:
                res.append(list(path))
                return
            # explore the neighbor nodes one after another.
            for nextNode in graph[currNode]:
                path.append(nextNode)
                backtrack(nextNode, path)
                path.pop()
        # kick of the backtracking, starting from the source node (0).
        path = deque([0])
        backtrack(0, path)

        return res