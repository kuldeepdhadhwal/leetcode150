class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        total_count = 0
        for i in nums:
            if i%3 != 0:
                total_count += 1
        return total_count
