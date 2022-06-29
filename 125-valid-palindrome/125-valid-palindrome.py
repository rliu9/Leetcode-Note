class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""  
        for c in s.lower():
            if c.isalpha() or c.isdigit():
                text += c
        return text == text[::-1]