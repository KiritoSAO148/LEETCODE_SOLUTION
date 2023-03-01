class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == int(str(abs(x))[::-1]): return True
        return False