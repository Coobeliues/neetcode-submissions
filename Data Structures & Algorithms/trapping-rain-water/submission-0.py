class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_mx, r_mx = height[l], height[r]
        res = 0

        while l < r:
            if l_mx < r_mx:
                l += 1
                l_mx = max(l_mx, height[l])
                res += l_mx - height[l]
            else:
                r -= 1
                r_mx = max(r_mx, height[r])
                res += r_mx - height[r]
        
        return res