class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in num_set:
                largest = 1
                while (num + largest) in num_set:
                    largest +=1
                longest = max(largest,longest)
        return longest
