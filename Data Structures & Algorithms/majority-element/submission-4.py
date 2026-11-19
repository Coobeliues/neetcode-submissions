class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt, cand = 1, nums[0]

        for i in nums[1:]:
            if i == cand:
                cnt += 1
            elif cand != i and cnt == 0:
                cand = i
            else: cnt -= 1
        
        return cand
