class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def converter(c):
            return ord(c) - ord('0')
        x,y = 0,0
        for i in num1: x = x*10 + converter(i)
        for j in num2: y = y*10 + converter(j)
        return str(x+y)
