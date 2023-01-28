class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        l = [-i for i in nums]
        heapq.heapify(l)
        res = [float('inf')] * 3
        for i in range(min(len(l), 3)):
            res[i] = heapq.heappop(l)
        return -res[-1] if res[-1] != float('inf') else -min(res)