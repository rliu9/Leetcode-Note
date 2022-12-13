class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = r = 0
        for i in range(len(s)):
            odd = self.helper(s, i, i)
            even = self.helper(s, i, i+1)
            l,r = max(odd, even, (l,r), key=lambda x:x[1]-x[0])
        return s[l:r]

    def helper(self, s, l, r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return (l+1,r)
    
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    
if __name__ == '__main__':
    s = Solution()
    #assert s.longestPalindrome("babad") == "aba"
    
    