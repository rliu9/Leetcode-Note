class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_size = sum(data)
        num_ones = sum(data[:window_size])
        max_ones = num_ones
        for i in range(window_size, len(data)):
            j = i-window_size
            num_ones = num_ones + data[i] - data[j]
            max_ones = max(num_ones, max_ones)
        return window_size - max_ones
    
    """
    Idea:
    Number of all 1's - max_ones(contains most 1's with window size) = minimum number of swaps 
    """
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)