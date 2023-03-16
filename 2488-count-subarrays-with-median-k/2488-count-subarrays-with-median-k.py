class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        freq = Counter({0 : 1})
        ans = diff = found = 0
        for x in nums: 
            if x < k: diff -= 1
            elif x > k: diff += 1
            else: found = 1
            if found: ans += freq[diff] + freq[diff-1]
            else: freq[diff] += 1
        return ans 