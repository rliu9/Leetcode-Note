class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,res = 0,0
        d = collections.defaultdict(int)
        for j in range(len(s)):
            if s[j] in d:
                i = max(i, d[s[j]]+1)
            res = max(res, j-i+1)
            d[s[j]] = j
        return res
    
    # time complexity: O(n)
    # space complexity: O(n)
    
if __name__ == '__main__':
    """
    abcabcbb
    i = 0; j = 3 -> res = 3 -> string: abc
    i = 1; j = 4 -> string: bca
    i = 2; j = 5 -> string: cab
    i = 3; j = 6 -> string: abc
    i = 5; j = 7 -> string: cb
    """
    assert 3 == Solution().lengthOfLongestSubstring("abcabcbb")
    assert 1 == Solution().lengthOfLongestSubstring("bbbbb")
    assert 3 == Solution().lengthOfLongestSubstring("pwwkew")