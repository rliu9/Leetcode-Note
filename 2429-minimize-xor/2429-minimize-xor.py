class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        s = "{0:b}".format(num2)
        ss = "{0:b}".format(num1)
        l = max(len(s),len(ss))
        
        s =''.join(['0']*(l-len(s)))+s
        ss =''.join(['0']*(l-len(ss)))+ss
        
        c1 = s.count('1')
        c0 = s.count('0')
        ress = []
        i = 0
        while i < len(ss) and c1 > 0 and c0 > 0:
            if ss[i] == '0':
                ress.append('0')
                c0 -= 1
            else:
                ress.append('1')
                c1 -= 1
            i += 1
        
        if c1:ress += ['1']*c1
        if c0:ress += ['0']*c0
        return int(''.join(ress), 2)