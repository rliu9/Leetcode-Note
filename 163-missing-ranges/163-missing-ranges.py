class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        for n1, n2 in zip([lower-1, *nums], [*nums, upper+1]):
            if n2 - n1 == 2:
                ans.append(str(n1 + 1))
            elif n2 - n1 > 2:
                ans.append(str(n1+1) + "->" + str(n2 - 1))
        return ans
    
    # O(n)
    # O(1)
