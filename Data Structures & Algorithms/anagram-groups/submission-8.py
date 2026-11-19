class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            
            key = tuple(cnt)
            if key not in d:
                d[key] = []
            d[key].append(s)
        
        return list(d.values())