class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        z, f, s = 0, 1, 1
        for _ in range(3, n + 1):
            curr = z + f + s
            z = f
            f = s
            s = curr
        
        return s