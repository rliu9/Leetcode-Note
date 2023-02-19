class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = collections.Counter(s)
        idx = 0
        for i in range(len(s)):
            if s[idx] > s[i]:
                idx = i
            c[s[i]] -= 1
            if c[s[i]] == 0:break
        return s[idx] + self.removeDuplicateLetters(s[idx:].replace(s[idx], '')) if s else ''
    
    # O(n) recursive calls is bounded by 26 O(n) * 26
    # O(n) we're creating a new string while slicing