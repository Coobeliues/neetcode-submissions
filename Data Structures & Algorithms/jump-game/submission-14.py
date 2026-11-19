class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0

        for i, jump in enumerate(nums):
            if i > mx:
                return False
            mx = max(mx, i + jump)

            if mx > len(nums) - 2:
                return True
        
        return True