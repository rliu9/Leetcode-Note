class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, res = 0, len(height)-1, 0
        lmax, rmax = height[0], height[-1]
        while l < r:
            if height[l] < height[r]:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax-height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax-height[r]
        return res