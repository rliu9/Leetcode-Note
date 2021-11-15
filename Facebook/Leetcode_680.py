class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                ss = s[:left] + s[left+1:]
                if ss == ss[::-1]: return True
                ss = s[:right] + s[right+1:]
                if ss == ss[::-1]: return True
                else:
                    return False
        return True
