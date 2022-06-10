class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
            
        power = x
        multiplications = 1
        while n - multiplications * 2 >= 0:
            power *= power
            multiplications *= 2

        return power * self.myPow(x, n - multiplications)