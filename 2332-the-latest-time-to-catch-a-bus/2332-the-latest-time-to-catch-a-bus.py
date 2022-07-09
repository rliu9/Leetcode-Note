class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        
        passenger = 0
        for bus in buses:
            maxed_out = False
            cap = capacity
            
            while passenger < len(passengers) and passengers[passenger] <= bus and cap != 0:
                passenger += 1
                cap -= 1
                
            if cap == 0:
                maxed_out = True
                
        if maxed_out:
            max_seat = passengers[passenger - 1]
        else:
            max_seat = buses[-1]
    
        booked = set(passengers)
        
        for seat in range(max_seat, 0, -1):
            if seat not in booked:
                return seat