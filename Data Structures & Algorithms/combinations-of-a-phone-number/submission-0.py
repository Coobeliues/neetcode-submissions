class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []

        def back(start, path):
            if len(path) == len(digits):
                res.append(''.join(path))
                return 
            
            for i in range(start, len(digits)):
                for char in phone[digits[i]]:
                    path.append(char)
                    back(i + 1, path)
                    path.pop()
        
        back(0, [])

        return res