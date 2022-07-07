class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for _ in range(1, n):
            count, temp, num = 0, '', res[0]
            for i in res:
                if num == i:
                    count += 1
                else:
                    temp += str(count) + num
                    num = i
                    count = 1
            temp += str(count) + num   
            res = temp
        return res