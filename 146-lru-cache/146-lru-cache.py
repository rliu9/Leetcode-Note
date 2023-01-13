class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.od = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key)
            return self.od[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.move_to_end(key)
        else:
            if len(self.od) >= self.capacity:
                for k,v in self.od.items():
                    self.od.pop(k)
                    break
        self.od[key] = value
        
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)