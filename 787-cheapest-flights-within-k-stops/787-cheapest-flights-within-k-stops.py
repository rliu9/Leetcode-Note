class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        neis = collections.defaultdict(list)
        for f, t, p in flights:
            neis[f].append((t, p))
            
        heap = [(0, k, src)]
        seen_stops = collections.defaultdict(int)

        while heap:
            totalP, stops, city = heapq.heappop(heap)
            if city == dst:
                return totalP
            if stops < 0:
                continue
            if city in seen_stops and seen_stops[city] >= stops:
                continue
            seen_stops[city] = stops
            
            for nei, neiP in neis[city]:
                heapq.heappush(heap, (totalP + neiP, stops - 1, nei))
        
        return -1