class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        first = 1
        second = 2
        total_steps = 0
        for i in range(2,n):
            total_steps = first + second
            first = second
            second = total_steps
        print(total_steps)
        return total_steps
