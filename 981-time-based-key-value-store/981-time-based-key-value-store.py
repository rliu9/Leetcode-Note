class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.d:
            li, n = self.d[key], len(self.d[key])
            l, r = 0, n-1
            if li[l][0] > timestamp:return ''
            while l <= r:
                mid = l + (r-l) // 2
                if li[mid][0] == timestamp:return li[mid][1]
                if li[mid][0] < timestamp:l = mid + 1
                else:r = mid - 1
            return li[r][1]
        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)