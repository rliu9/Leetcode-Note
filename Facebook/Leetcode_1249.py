# my solution
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        stack2 = []
        _set = set()
        for i in range(len(s)):
            if s[i].isdigit(): continue
            else:
                if s[i] == '(':
                    if '(' not in stack:
                        stack.append(i)
                elif s[i] == ')':
                    if stack:
                        stack.pop()
                    else:
                        stack2.append(i)
        ans = []
        for i in range(len(s)):
            if i not in stack and i not in stack2:
                ans.append(s[i])
        return ''.join(ans)



# optimal solution
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        _set = set()
        for i,char in enumerate(s):
            if char not in '()':
                continue
            elif char == '(':
                stack.append(i)
            elif char == ')':
                if not stack:
                    _set.add(i)
                else:
                    stack.pop()
        _set = _set.union(set(stack))
        res = []
        for i,char in enumerate(s):
            if i not in _set:
                res.append(char)
        return "".join(res)
"""
