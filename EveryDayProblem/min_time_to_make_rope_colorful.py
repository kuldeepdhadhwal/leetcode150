from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = max_cost = 0

        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i-1]:
                max_cost = 0
            res += min(max_cost, neededTime[i])
            max_cost = max(max_cost,neededTime[i])
        
        return res



#two pointer approach
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = 0
        res = 0
        r=1

        while r < len(colors):
            if colors[l] == colors[r]:
                #check which one is min
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    l = r
                else:
                    res += neededTime[r]
            else:
                l = r
        
        return res