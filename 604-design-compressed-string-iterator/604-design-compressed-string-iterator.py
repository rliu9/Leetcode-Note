class StringIterator:

    """ def __init__(self, compressedString: str):
        string = compressedString
        self.stack = []
        i = len(string)-1
        ch, n = '', ''
        while i >= 0:
            temp = string[i]
            if temp.isalpha():
                for _ in range(int(n[::-1])):
                    self.stack.append(temp)
                i -= 1
                n = ''
            else:
                while string[i].isdigit():
                    n += string[i]
                    i -= 1

    def next(self) -> str:
        if not self.stack:return ' '
        return self.stack.pop()

    def hasNext(self) -> bool:
        return len(self.stack) > 0"""

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        #first:extract letter from string, and replace letter with blank e.g."x16a2" -> " 16 2"
        self.letter = []
        for i in compressedString:   
            if i.isalpha():
                self.letter.append(i)
                compressedString = compressedString.replace(i, ' ')

       #second:extract number and convert it to int from modified string 
        self.number = [int(i) for i in compressedString.split()]

    def next(self):
        """
        :rtype: str
        """
        if self.number:
            if self.number[0] > 0:          
                n = self.letter[0]
                self.number[0] -= 1
                if self.number[0] == 0:
                    del self.letter[0]            
                    del self.number[0]          
                return n       
        else:
            return ' '


    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.number else False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()