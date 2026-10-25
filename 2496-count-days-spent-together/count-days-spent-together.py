class Solution:
    
    def getDay(self,date:str) ->int:

        days = [
            31,28,31,30,31,30,
            31,31,30,31,30,31
        ]
        month, day = map(int,date.split("-"))

        total = sum(days[:month-1])

        total+=day
        return total

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice_start = self.getDay(arriveAlice)
        alice_end = self.getDay(leaveAlice)

        bob_start = self.getDay(arriveBob)
        bob_end = self.getDay(leaveBob)

        start = max(alice_start,bob_start)

        end = min(alice_end,bob_end)

        if start > end:
            return 0

        return end- start+1

        