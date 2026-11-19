class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt, prod = 0, 1
        res = [0] * len(nums)

        for i in nums:
            if i:
                prod *= i
            else: cnt += 1

        if cnt > 1:
            return res

        
        
        for i, c in enumerate(nums):
            if cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        
        return res