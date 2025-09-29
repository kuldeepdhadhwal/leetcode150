# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/1786105126/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_0 = 0
        if nums[l] < nums[r] or len(nums) >=1:
            return min(nums)
        else:
            l=0
            r=1
            while l < r and r < len(nums):
                if nums[l] < nums[r]:
                    l = r
                    r +=1
                    print(r)
                    # print(nums[l])
                else:
                    print(r)
                    min_0 = nums[r]
                    return min_0
        return min_0
        
