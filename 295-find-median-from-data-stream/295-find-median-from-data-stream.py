class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.l, num)

    def findMedian(self) -> float:
        if len(self.l) % 2 != 0:return self.l[len(self.l)//2]
        return (self.l[len(self.l)//2] + self.l[len(self.l)//2-1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()