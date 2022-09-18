class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        di = {0:'qwertyuiopQWERTYUIOP', 1:'asdfghjklASDFGHJKL', 2:'zxcvbnmZXCVBNM'}
        res = []
        for word in words:
            for d in di:
                if word[0] in di[d]:key = d
            check = True
            for w in word:
                if w not in di[key]:
                    check = False
                    break
            if check:res.append(word)
        return res