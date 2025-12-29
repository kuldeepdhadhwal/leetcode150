class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        max_rob = 0
        for num in nums:
            max_rob = max(num+rob1,rob2)
            rob1 = rob2
            rob2 = max_rob
        return rob2


# dynamic programming
def rob(arr, i=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if i >= len(arr):
        return 0
    if i in lookup:
        return lookup[i]
    else:
        lookup[i] = max(arr[i]+rob(arr, i+2,lookup), rob(arr, i+1,lookup))
        return lookup[i]
arr = [2, 10, 3, 6, 8, 1, 7]        
res = rob(arr)
print(res)
