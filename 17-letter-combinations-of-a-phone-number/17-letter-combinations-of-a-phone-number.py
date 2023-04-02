class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        res = []
        for i in digits:
            res.append(phone[int(i)])
        print(res)
        while len(res) > 1:
            l1 = res.pop()
            l2 = res.pop()
            temp = []
            for i in l2:
                for j in l1:
                    temp.append(i+j)
            res.append(temp)
        return res[0] if res else []