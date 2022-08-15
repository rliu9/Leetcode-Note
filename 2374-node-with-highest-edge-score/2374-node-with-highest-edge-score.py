class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        d = collections.defaultdict(int)
        for i, edge in enumerate(edges):
            d[edge] += i
        maximum = max(d.values())
        for i in sorted(d):
            if d[i] == maximum:return i