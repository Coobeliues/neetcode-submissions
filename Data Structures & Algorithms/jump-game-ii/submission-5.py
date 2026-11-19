class Solution:
    def jump(self, nums: List[int]) -> int:
        j, curr, far = 0, 0, 0
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            
            if i == curr:
                j += 1
                curr = far

                if curr >= len(nums) - 1:
                    break
        
        return j