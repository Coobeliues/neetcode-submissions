class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            cnt = sum(1 for num in nums if num <= m)
            if cnt > m:
                r = m
            else: l = m + 1
        
        return l