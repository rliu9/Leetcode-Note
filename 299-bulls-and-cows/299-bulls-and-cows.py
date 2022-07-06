class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s,g = Counter(secret),Counter(guess)
        a = sum(i==j for i,j in zip(secret,guess))
        return str(a)+'A'+str(sum((s&g).values())-a)+'B'