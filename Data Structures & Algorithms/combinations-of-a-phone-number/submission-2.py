class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []

        def back(i, curr):
            if i == len(digits):
                res.append(curr)
                return 

            for char in phone[digits[i]]:
                back(i + 1, curr + char)
        
        back(0, '')

        return res