class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0
        stack = []
        opt = ['+', '-', '*', '/']
        op = '+'
        cur = 0
        s = s.replace(' ', '')
        for index,i in enumerate(s):
            if i.isdigit(): cur = cur*10 + int(i)
            if i in opt or index == len(s)-1:
                if op == '+': stack.append(cur)
                elif op == '-': stack.append(-cur)
                elif op == '*': stack[-1] = stack[-1]*cur
                elif op == '/': stack[-1] = int(stack[-1]/cur)
                op,cur = i,0
        return sum(stack)
