class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        res, m, left = 0, 0, 0
        for right in range(len(s)):
            count[s[right]] += 1
            m = max(m, count[s[right]])
            if right-left+1-m > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res