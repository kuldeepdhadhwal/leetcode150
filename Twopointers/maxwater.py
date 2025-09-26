class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        max_water = 0
        while l < r:
            current_capacity = 0
            if heights[l] < heights[r]:
                current_capacity = heights[l]*abs((r-l))
                max_water = max(current_capacity, max_water)
                l +=1
            elif heights[l] > heights[r]:
                current_capacity = heights[r]*abs((l-r))
                max_water = max(current_capacity, max_water)
                r -=1
            else:
                current_capacity = heights[l]*abs((l-r))
                max_water = max(current_capacity, max_water)
                l +=1
                r -=1
        return max_water
