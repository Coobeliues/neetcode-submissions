class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for i in s:
                cnt[ord(i) - ord('a')] += 1
            cnt = tuple(cnt)
            res[cnt].append(s)
        
        return list(res.values())
        
