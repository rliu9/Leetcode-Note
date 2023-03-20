class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.res = 0
        s = []
        def bc(idx):
            if idx == len(nums):return
            for i in range(idx, len(nums)):
                if nums[i]+k in s or nums[i]-k in s:continue
                self.res += 1
                s.append(nums[i])
                bc(i+1)
                s.pop()
        bc(0)
        return self.res