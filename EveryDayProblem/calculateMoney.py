class Solution:
    def totalMoney(self, n: int) -> int:
        total_money = 0
        start_week = 1

        for i in range(1,n+1):
            total_money += start_week
            start_week +=1
            if i%7 == 0:
                start_week = int(i/7) +1
        return total_money
