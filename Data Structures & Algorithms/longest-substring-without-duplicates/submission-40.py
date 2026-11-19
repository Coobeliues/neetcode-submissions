class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        d = {}
        mx = 0

        for r in range(len(s)):
            if s[r] in d:
                l = max(d[s[r]] + 1, l)
            d[s[r]] = r
            mx = max(mx, r - l + 1)
        
        return mx 