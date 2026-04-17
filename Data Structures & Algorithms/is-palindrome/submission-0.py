class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        r = reversed(s)
        r = "".join(r)

        if s == r :
            return True
        else :
            return False
        