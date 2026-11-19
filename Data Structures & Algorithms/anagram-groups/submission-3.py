class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for i in strs:
            count = [0] * 26

            for j in i:
                count[ord(j) - ord('a')] += 1
            
            count = tuple(count)
            if count in res:
                res[count].append(i)
            else: res[count] = [i]
        
        return list(res.values())