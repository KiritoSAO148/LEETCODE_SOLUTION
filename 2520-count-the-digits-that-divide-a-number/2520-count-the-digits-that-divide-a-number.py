class Solution:
    def countDigits(self, num: int) -> int:
        tmp = num
        cnt = 0
        while tmp != 0:
            r = tmp % 10
            if num % r == 0: cnt += 1
            tmp //= 10
        return cnt