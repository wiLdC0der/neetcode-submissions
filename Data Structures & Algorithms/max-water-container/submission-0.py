class Solution:
    def maxArea(self, heights: List[int]) -> int:

        r = 0
        l = len(heights)-1

        area = 0

        while r <= l:
            maximum = (l-r) * min(heights[r],heights[l])
            area = max(area,maximum)
            if heights[r] < heights[l]:
                r+=1
            else:
                l-=1
        return area
        