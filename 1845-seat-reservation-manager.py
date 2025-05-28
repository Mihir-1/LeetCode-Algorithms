import heapq

class SeatManager:

    def __init__(self, n: int):
        self.seats = []
        self.nextSeat = 1

    def reserve(self) -> int:
        if self.seats:
            return heapq.heappop(self.seats)
        
        res = self.nextSeat
        self.nextSeat += 1
        return res

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)

'''
Time: O(r log(n))
Space: O(n)
'''

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
