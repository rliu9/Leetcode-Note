class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        last_node, res = len(graph) - 1, []
        def backtracking(cur_node, path):
            if cur_node == last_node:
                res.append(path[:])
                return
            for i in graph[cur_node]:
                path.append(i)
                backtracking(i, path)
                path.pop()
        backtracking(0,[0])
        return res
    # time complexity: O(2^N * N)
    # space complexity: O(2^N * N)