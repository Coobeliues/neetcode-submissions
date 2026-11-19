class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        mn = r
        while l <= r:
            m = l + (r - l) // 2
            k = 0
            for i in piles:
                k += (i + m - 1) // m
                if k > h:
                    break
            if k <= h:
                mn = m
                r = m - 1
            else: l = m + 1

        return mn
