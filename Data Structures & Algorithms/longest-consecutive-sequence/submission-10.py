class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        cnt = 1
        mx = 0

        for i in seen:
            if i - 1 not in seen:
                while i + cnt in seen:
                    cnt += 1
            mx = max(mx, cnt)
            cnt = 1
        
        return mx