class Solution:
    def partitionString(self, s: str) -> int:
        cur = ''
        res = 1
        for i in s:
            if i in cur:
                res += 1
                cur = i
            else:
                cur += i
        return res
    
    #O(n)
    #O(n)