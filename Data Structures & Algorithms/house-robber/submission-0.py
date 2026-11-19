class Solution:
    def rob(self, nums: List[int]) -> int:
        f, s = 0, 0

        for i in nums:
            curr = max(i + f, s)
            f = s
            s = curr
        
        return curr