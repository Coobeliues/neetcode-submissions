class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        seen = set()
        l, r = 0, 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                
            elif s[r] in seen:
                seen = set()
                l += 1
                r = l 

            
            mx = max(mx, r - l)
            
        return mx