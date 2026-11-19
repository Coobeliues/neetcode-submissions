class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_min, curr_max = 1, 1

        for n in nums:
            tmp = n * curr_max

            curr_max = max(n * curr_max, n * curr_min, n)
            curr_min = min(tmp, n * curr_min, n)

            res = max(curr_max, res)
        
        return res