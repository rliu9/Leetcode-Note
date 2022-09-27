class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in tokens:
            if i not in '+-*/':
                stack.append(i)
            else:
                second = stack.pop()
                first = stack.pop()
                stack.append(int(eval(f'{first} {i} {second}')))
        return stack[-1]