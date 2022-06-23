class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_size = sum(data)
        num_ones = sum(data[0:window_size])
        max_ones = num_ones
        for i in range(window_size, len(data)):
            j = i - window_size
            num_ones -= data[j]
            num_ones += data[i]
            max_ones = max(max_ones, num_ones)
        return window_size - max_ones