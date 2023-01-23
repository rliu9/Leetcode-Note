class RandomizedSet:

    def __init__(self):
        self.d, self.l = {}, []

    def insert(self, val: int) -> bool:
        if val in self.d:return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.d:
            last, i = self.l[-1], self.d[val]
            self.l[i], self.d[last] = last, i
            self.l.pop()
            del self.d[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()