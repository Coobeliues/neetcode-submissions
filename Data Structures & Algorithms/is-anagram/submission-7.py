class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        z, d = {}, {}
        
        for i in s:
            z[i] = z.get(i, 0) + 1
        for j in t:
            d[j] = d.get(j, 0) + 1
        
        return z == d