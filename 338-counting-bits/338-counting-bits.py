class Solution:
    def countBits(self, n: int) -> List[int]:
        return ["{0:b}".format(i).count("1") for i in range(n+1)]