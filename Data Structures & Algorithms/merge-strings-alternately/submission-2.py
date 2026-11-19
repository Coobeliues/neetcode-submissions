class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        s = ''
        while l < len(word1) and r < len(word2):
            s += word1[l]
            l += 1
            s += word2[r]
            r += 1
        
        if r == len(word2):
            s += word1[l:]
        elif l == len(word1):
            s += word2[r:]

        return s