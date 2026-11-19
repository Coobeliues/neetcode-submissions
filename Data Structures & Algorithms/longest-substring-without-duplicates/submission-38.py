class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        d = {}

        for r in range(len(s)):
            if s[r] in d:
                l = max(d[s[r]] + 1, l)
            d[s[r]] = r
            res = max(res, r - l + 1)    
        return res