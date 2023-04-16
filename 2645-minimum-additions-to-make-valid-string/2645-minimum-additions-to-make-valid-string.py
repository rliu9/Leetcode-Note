class Solution:
    def addMinimum(self, word: str) -> int:
        stack = list(word)
        i = 0
        while stack:
            if stack and stack[-1] == 'c':
                stack.pop()
            else:
                i += 1
            if stack and stack[-1] == 'b':
                stack.pop()
            else:
                i += 1
            if stack and stack[-1] == 'a':
                stack.pop()
            else:
                i += 1
        return i