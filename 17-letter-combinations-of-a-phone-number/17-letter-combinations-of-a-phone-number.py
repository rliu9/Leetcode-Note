class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numbers = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res = []
        for i in digits:
            res.append(numbers[i])
        while len(res) > 1:
            l1 = res.pop()
            l2 = res.pop()
            add = []
            for i in l2:
                for j in l1:
                    add.append(i+j)
            res.append(add)
        return res[0] if res else []
    
    # O(N*4^N)
    # O(N)