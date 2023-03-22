class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            res, tmp = '', n
            while tmp != 0:
                res = str(tmp % i) + res
                tmp //= i
            if res != res[::-1]: return False
        return True
                