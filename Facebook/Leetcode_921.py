class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        _set = set()
        stack = []
        stack2 = []
        for i in s:
            if i == '(': stack.append(i)
            else: 
                if stack and stack[-1] == '(': stack.pop()
                else: stack2.append(i)
        return len(stack)+len(stack2)
      
      
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        stack2 = []
        for i in s:
            if stack and i == ')': stack.pop()
            elif i == '(': stack.append(i)
            else: stack2.append(i)
        return len(stack)+len(stack2)
