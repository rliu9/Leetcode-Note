class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':stack.append(')')
            elif c == '{':stack.append('}')
            elif c == '[':stack.append(']')
            else:
                if not stack or stack.pop() != c:return False
        return not stack
    
    # O(n)
    # O(n)