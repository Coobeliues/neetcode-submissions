class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        next1, next2 = 1, 0
        
        for i in range(n - 1, -1, -1):
            curr = 0
            if s[i] != '0':
                curr += next1

            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                curr += next2 
            next2 = next1
            next1 = curr

        return next1        