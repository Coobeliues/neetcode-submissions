class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        mx = 0
        for i in nums:
            if i - 1 not in seen:
                cnt = 1
                while i + cnt in seen:
                    cnt += 1
                mx = max(mx, cnt)
        
        return mx