class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0: return 0
        if num < k: return -1
        if k == 0: return 1 if num % 10 == 0 else -1
        res = 0 
        while num:
            num -= k 
            res += 1
            if num < 0: return -1
            if num % 10 == 0:
                return res
        return -1
        