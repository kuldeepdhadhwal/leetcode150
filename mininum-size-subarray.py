class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_ = float('inf')
        left = 0
        total = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                total = total - nums[left]
                min_ = min(min_,right - left +1)
                left +=1
        return min_ if min_ != float('inf') else 0
