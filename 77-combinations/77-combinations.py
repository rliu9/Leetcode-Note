class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations([i for i in range(1, n+1)], k)
    
if __name__ == '__main__':
    output = [
        [2,4],
        [3,4],
        [2,3],
        [1,2],
        [1,3],
        [1,4],
    ]
    #assert sorted(output) == sorted(Solution().combine(4, 2))