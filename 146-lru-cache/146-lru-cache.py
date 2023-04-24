class LRUCache:

    def __init__(self, capacity: int):
        self.od = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key, last=False)
            return self.od[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.od[key] = value
        self.od.move_to_end(key, last=False)
        if len(self.od) > self.capacity:
            self.od.popitem(last=True)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)