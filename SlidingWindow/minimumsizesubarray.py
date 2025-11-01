class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 1
        current_sum = 0
        result = float(inf)
        for right in range(len(nums)):
            current_sum +=nums[right]

            while current_sum >= target:
                current_sum -= nums[left]
                result = min(result, right-left+1)
                left +=1
        return 0 if result == inf else result