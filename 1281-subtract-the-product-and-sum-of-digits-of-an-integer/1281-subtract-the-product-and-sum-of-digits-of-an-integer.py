class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p = 0, 1
        while n != 0:
            r = n % 10
            s += r
            p *= r
            n //= 10
        return p - s