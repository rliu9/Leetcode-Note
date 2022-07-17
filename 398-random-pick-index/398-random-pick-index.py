class Solution:

    def __init__(self, nums: List[int]):
        self.hash = collections.defaultdict(list)
        for i,n in enumerate(nums):
            self.hash[n].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.hash[target]) # O(1)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)