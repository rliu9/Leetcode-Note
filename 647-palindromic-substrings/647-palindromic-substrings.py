class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            odd = self.helper(s, i, i)
            even = self.helper(s, i, i+1)
            res += odd + even
        return res
    
    def helper(self, s, l, r):
        ret = 0
        while l>=0 and r<len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            ret += 1
        return ret
    
    # O(n)
    # O(n)
    
if __name__ == '__main__':
    s = Solution()
    assert s.countSubstrings('nnonn') == 9