class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r, res = 1, max(piles), 0
        while l <= r:
            mid = (l+r) // 2
            time = sum(math.ceil(pile/mid) for pile in piles)
            if time > h:
                l = mid + 1
            else:
                r = mid - 1
                res = mid
        return res