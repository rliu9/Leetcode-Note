class Solution:
    def countBits(self, n: int) -> List[int]:
        #return ["{0:b}".format(i).count("1") for i in range(n+1)]
        res = []
        for i in range(n+1):
            val = i
            n = 0
            while val > 0:
                val = val & (val-1)
                n += 1
            res.append(n)
        return res
    
    # O(nlogn)
    # O(1)