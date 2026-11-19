class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one = 1
        two = 1
        i = 0

        while i < n - 1:
            current = one
            one = one + two
            two = current
            i += 1
        
        return one