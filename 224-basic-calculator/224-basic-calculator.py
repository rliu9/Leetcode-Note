class Solution:
    def calculate(self, s: str) -> int:
        num, sign, stack = 0, 1, [0]
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            elif i == '+':
                stack[-1] += num * sign
                num = 0
                sign = 1
            elif i == '-':
                stack[-1] += num * sign
                num = 0
                sign = -1
            elif i == '(':
                stack.extend([sign, 0])
                num = 0
                sign = 1
            elif i == ')':
                lastNum = (stack.pop() + num*sign) * stack.pop()
                stack[-1] += lastNum
                num, sign = 0, 1
        return stack[-1] + num*sign
    
    
        
        