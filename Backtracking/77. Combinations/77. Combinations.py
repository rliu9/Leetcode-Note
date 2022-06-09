class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        add, res = [], []
        def backtracking(idx):
            if len(add) == k:
                res.append(add[:])
            for i in range(idx, n+1):
                add.append(i)
                backtracking(i+1)
                add.pop()
        backtracking(1)
        return res
    
    # time complexity: O(2^n)
    # space complexity: n!/(n-k)!k! -> # of combinations to build
    
if __name__ == '__main__':
    output = [
        [2,4],
        [3,4],
        [2,3],
        [1,2],
        [1,3],
        [1,4],
    ]
    assert sorted(output) == sorted(Solution().combine(4, 2))
