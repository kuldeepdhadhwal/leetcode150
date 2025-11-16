class Solution:
    def numSub(self, s: str) -> int:
        # count = 0
        # total = 0
        # mod = 1000000007
        # for a in s:
        #     if a == '1':
        #         count +=1
        #     else:
        #         count = 0

        #     total = (total+count)% mod
        # return total
        total = 0
        MOD = 10**9 + 7
        for a in s.split('0'):
            n= len(a)
            count = (n*(n+1))//2
            total += count
        return total % MOD