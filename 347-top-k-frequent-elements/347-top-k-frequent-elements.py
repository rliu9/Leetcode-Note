class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        return heapq.nlargest(k, c.keys(), key=c.get)
    
    # Time Complexity: O(N logK)
    # Space Complexity: O(N+k)