class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.cur = nums[:]

    def reset(self) -> List[int]:
        self.cur = self.nums
        return self.cur

    def shuffle(self) -> List[int]:
        self.cur = random.sample(self.cur, len(self.cur))
        return self.cur


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()