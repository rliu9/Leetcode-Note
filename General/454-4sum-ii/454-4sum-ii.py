class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashtable = defaultdict(int)
        count = 0
        for i in nums1:
            for j in nums2:
                hashtable[i+j] += 1
        for i in nums3:
            for j in nums4:
                count += hashtable[-(i+j)]
        return count
    
    # O(n^2)
    # O(n^2)