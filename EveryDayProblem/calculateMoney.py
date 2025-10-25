class Solution:
    def totalMoney(self, n: int) -> int:
        total_amount = 0
        day_amount = 1
        week_start = 1

        for i in range(1,n+1):
            total_amount += day_amount
            day_amount+=1
            if int(i%7) == 0:
                week_start +=1
                day_amount = week_start

        return total_amount