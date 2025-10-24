class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter
        count = Counter(s)
        print(count)
        
        max_result = 0
        max_even = float('inf')
        max_odd  = 0
        for key, val in count.items():
            if val % 2 == 0:
                max_even =  min(val,max_even)
            else:
                max_odd = max(max_odd,val)
        if max_even == float('inf'):
            return max_odd
        result = max_odd - max_even
        return result
