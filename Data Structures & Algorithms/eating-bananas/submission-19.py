class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) 
        while l < r:
            k = l + (r - l) // 2
            sm = 0
            for p in piles:
                sm += (p + k - 1) // k
            if sm <= h:
                r = k
            else: l = k + 1

        return l         