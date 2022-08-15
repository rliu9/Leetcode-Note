class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for x in zip(*strs):
            if len(set(x)) == 1:
                i += 1
            else:
                break
        return strs[0][:i]
    
    # Time Complexity: O(min(len) * n)
    # Space Complexity: O(1)