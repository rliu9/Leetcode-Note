class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate(num):
            _sum = 0
            while num:
                _sum += (num%10)**2
                num = num // 10
            return _sum
        record = set()
        while n != 1:
            n = calculate(n)
            if n in record:
                return False
            else:
                record.add(n)
        return True