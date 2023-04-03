class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # bfs
        if not digits:return
        phone_letters = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        q = deque(phone_letters[int(digits[0])])
        for i in range(1,len(digits)):
            s = len(q)
            while s:
                out = q.popleft()
                for j in phone_letters[int(digits[i])]:
                    q.append(out + j)
                s -= 1
                
        return q