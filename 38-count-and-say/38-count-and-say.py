class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for _ in range(1, n):
            count, next_res, cur = 0, '', res[0]
            for i in res:
                if i == cur:
                    count += 1
                else:
                    next_res += str(count)
                    next_res += cur
                    cur = i
                    count = 1
            next_res += str(count)
            next_res += cur
            res = next_res
        return res