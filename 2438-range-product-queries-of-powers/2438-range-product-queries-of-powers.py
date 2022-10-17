class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers, res = [], []
        b = bin(n)[2:][::-1]
        for i, v in enumerate(b):
            if v == '1':
                powers.append(2**i)
        for q in queries:
            val = 1
            for i in range(q[0], q[1]+1):
                val *= powers[i]
            res.append(val%(10**9+7))
        return res