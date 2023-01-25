class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.l = []
        for i in vec:
            for j in i:
                self.l.append(j)

    def next(self) -> int:
        return self.l.pop(0)
        

    def hasNext(self) -> bool:
        return self.l


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()