class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        distance = ord('A') 

        while columnNumber > 0:
            y = (columnNumber-1) % 26
            columnNumber = (columnNumber-1) // 26
            s = chr(y+distance)
            result = ''.join((s, result))

        return result
            