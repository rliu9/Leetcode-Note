class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        A = [int(x) for x in num1.replace('i','').split('+')]
        B = [int(x) for x in num2.replace('i','').split('+')]
        return str(A[0]*B[0]-A[1]*B[1])+'+'+str(A[0]*B[1]+A[1]*B[0])+'i'