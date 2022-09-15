class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        a = itertools.permutations([i for i in range(1, n+1)], n)
        for i, n in enumerate(a):
            if i == k-1:
                return ''.join(map(str, list(n)))