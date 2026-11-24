class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def back(start, path):
            if start == len(s):
                res.append(path.copy())
                return
            

            for i in range(start, len(s)):
                sub = s[start: i + 1]
                
                if sub == sub[::-1]:
                    path.append(sub)
                    back(i + 1, path)
                    path.pop()
        
        back(0, [])

        return res