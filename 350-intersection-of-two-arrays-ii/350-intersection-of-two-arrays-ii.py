class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):
            return self.intersect(nums2, nums1)
        c = collections.Counter(nums1) # O(n)
        res = []
        for i in nums2: # O(m)
            if i in c:
                res.append(i)
                c[i] -= 1
                if c[i] == 0:del c[i]
        return res
    
    # O(m + n)
    # O(min(m, n))