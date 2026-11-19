class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        for i in range(len(first)):
            char = first[i]
            for s in strs[1:]:
                if i == len(s) or char != s[i]:
                    return first[:i]
        
        return first