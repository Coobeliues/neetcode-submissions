class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max = 0

        for i in nums:
            curr_max = max(curr_max + i, i)
            res = max(res, curr_max)
        
        return res