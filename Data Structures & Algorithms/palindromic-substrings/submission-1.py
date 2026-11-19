class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(set(s)) == len(s):
            return len(s)
        if len(set(s)) == 1:
            return (len(s) * (len(s) + 1)) // 2
        
        cnt = 0
        for i in range(len(s)):
            for l, r in [(i, i), (i, i + 1)]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    cnt += 1
                    l -= 1
                    r += 1
        
        return cnt