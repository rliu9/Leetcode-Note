class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        for start,end in sorted(intervals):
            if not heap or heap[0] > start:
                # rooms are still in use
                heapq.heappush(heap, end)
            else: # free room available , replace with current meeting
                heapq.heappop(heap)
                heapq.heappush(heap,end)
        return len(heap)
    
    # O(nlogn)
    # O(n)