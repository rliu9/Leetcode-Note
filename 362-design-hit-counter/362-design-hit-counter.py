class HitCounter:

    def __init__(self):
        self.q = collections.deque([])
        self.startIdx = -1

    def hit(self, timestamp: int) -> None:
        if self.startIdx == -1:
            self.startIdx = timestamp # init 1st
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while timestamp - self.startIdx >= 300 and self.q:
            self.q.popleft()
            if self.q:
                self.startIdx = self.q[0]
            else:
                self.startIdx = -1
        return len(self.q)
            


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)