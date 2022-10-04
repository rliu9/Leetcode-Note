class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1 and stones[0] != 0:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, y-x)
        return -stones[0] if stones else 0