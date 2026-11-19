class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s.replace(" ", "")
        s = ''.join(char.lower() for char in s if char.isalnum())
        # s.lower()
        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                return False
        
        return True