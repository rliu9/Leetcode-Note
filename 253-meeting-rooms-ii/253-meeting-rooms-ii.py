class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort(key=lambda x: x[0])
        for x, y in intervals:
            if not heap or heap[0] > x:
                # rooms are still in use
                heapq.heappush(heap, y)
            else: # free room available , replace with current meeting 
                heapq.heappushpop(heap,y)
        return len(heap)
    
    # O(nlogn)
    # O(n)