class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = Counter(nums1), Counter(nums2)
        res = []
        for i in c1:
            if i in c2:
                res += [i] * min(c1[i], c2[i])
        return res