class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            val = token
            if token in '+-*/':
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    val = first + second
                elif token == '-':
                    val = first - second
                elif token == '*':
                    val = first * second
                else:
                    val = int(first / second)
                stack.append(val)
            else:
                stack.append(int(val))
        return stack[0]