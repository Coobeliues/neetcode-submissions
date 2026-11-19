class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        

        while l < r:
            k = l + (r - l) // 2
            need_days = 1
            curr_w = 0

            for w in weights:
                if curr_w + w > k:
                    need_days += 1
                    curr_w = 0
                curr_w += w
            
            if need_days <= days:
                r = k
            else: l = k + 1
        
        return l