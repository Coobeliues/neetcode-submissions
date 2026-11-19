class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        mx = 0

        while l < r:
            mn = min(heights[l], heights[r])
            mx = max(mx, mn * (r - l))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            mn = min(heights[l], heights[r])
            mx = max(mx, mn * (r - l))

        
        return mx