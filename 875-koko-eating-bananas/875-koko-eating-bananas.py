class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = l + (r-l) // 2
            time = sum(math.ceil(pile/mid) for pile in piles)
            if time > h:
                l = mid + 1
            else:
                r = mid
        return l