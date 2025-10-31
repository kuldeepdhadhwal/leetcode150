from typing import List
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        store = {}

        for i in nums:
            if i in store:
                res.append(i)
            else:
                store[i] = 1
        return res