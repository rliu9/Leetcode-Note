class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        unpaired_chars = set()
        
        for char in s:
            if char not in unpaired_chars:
                unpaired_chars.add(char)
            else:
                unpaired_chars.remove(char)
        # if not in set: odd occurrence
        # if in set: even occurrence
        return len(unpaired_chars) <= 1