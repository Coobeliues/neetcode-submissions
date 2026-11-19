class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt, cand = 0, None
        for num in nums:
            if cnt == 0:
                cand = num
            
            if cand == num:
                cnt += 1
            else: cnt -= 1
        
        return cand