class Solution:
    def addMinimum(self, word: str) -> int:
        stack = list(word)
        res = 0
        while stack:
            if stack and stack[-1] == 'c':
                stack.pop()
            else:
                res += 1
            if stack and stack[-1] == 'b':
                stack.pop()
            else:
                res += 1
            if stack and stack[-1] == 'a':
                stack.pop()
            else:
                res += 1
        return res
    
    # O(n)
    # O(n)