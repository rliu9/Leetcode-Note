class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def bc(idx, cur):
            if len(cur) == k:
                res.append(cur)
                return
            for i in range(idx, n+1):
                bc(i+1, cur+[i])
        bc(1, [])
        return res