# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/?envType=daily-question&envId=2025-10-27
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev_count = 0
        i = 0

        while i < len(bank):
            current_count = bank[i].count('1')
            print(current_count)
            if current_count > 0:
                if prev_count > 0:
                    print(prev_count,current_count)
                    res +=prev_count * current_count
                prev_count = current_count
            i+=1
        return res