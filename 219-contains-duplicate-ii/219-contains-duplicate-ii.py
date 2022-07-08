class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        85% and 96%

        if k==0:return False
        i = 0
        d = defaultdict(int)
        for j in range(len(nums)):
            if nums[j] in d:
                return True
            if j - i == k:
                if d[nums[i]] == 1:
                    del d[nums[i]]
                else:
                    d[nums[i]] -= 1
                i += 1
            d[nums[j]] += 1
        return False"""
        
        d = {}
        for i,j in enumerate(nums):
            if j in d and i - d[j] <= k:
                return True
            d[j] = i
        return False
    
    # O(n)
    # O(n)
        
    
        
    
                