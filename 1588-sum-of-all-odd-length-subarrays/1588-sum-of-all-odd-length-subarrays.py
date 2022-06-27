class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        """
        # O(n^3)
        # O(1)
        
        res = sum(arr)
        for i,n in enumerate(arr):
            j = i + 2
            while j < len(arr):
                res += sum(arr[i:j+1])
                j += 2
        return res
        """
        
        res = 0
        p_sum = [0]*(len(arr)+1)
        
        for i in range(len(arr)):
            p_sum[i+1] += p_sum[i] + arr[i]

        for i, p in enumerate(p_sum):
            for j in range(i + 1, len(arr)+1, 2):
                res += p_sum[j] - p_sum[i] 
        return res
        
    
    # Prefix
    # O(n^2)
    # O(1)