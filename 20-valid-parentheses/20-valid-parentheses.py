class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(':stack.append(')')
            elif i == '[':stack.append(']')
            elif i == '{':stack.append('}')
            else:
                if not stack or stack.pop() != i:
                    return False
        return len(stack) == 0
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    
if __name__ == '__main__':
    assert True == Solution().isValid("()[]{}")
    assert False == Solution().isValid("(]")