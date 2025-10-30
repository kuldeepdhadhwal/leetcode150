# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/?envType=daily-question&envId=2025-10-30

from typing import List
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        totalOperations = target[0]
        for i in range(1,len(target)):
            if (target[i] > target[i-1]):
                totalOperations += target[i] - target[i-1]
        return totalOperations
    

# This will work like a stack where we only care about the previous height and current height to calculate the increments needed