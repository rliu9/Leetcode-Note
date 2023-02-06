class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1:"I",
            2:"II",
            3:"III",
            4:"IV",
            5:"V",
            6:"VI",
            7:"VII",
            8:"VIII",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M",
        }
        res = ''
        for i in reversed(d):
            amount = num // i
            res += amount*d[i]
            num -= amount*i
        return res
    
    # O(1)
    # O(1)