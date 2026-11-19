class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 0, x // 2
        res = 0
        while l <= r:
            m = l + (r - l) // 2
            m2 = m * m
            if m2 == x:
                return m
            if m2 < x:
                res = m
                l = m + 1
            else:
                r = m - 1
        
        return res