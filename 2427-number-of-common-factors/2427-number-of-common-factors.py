from math import *
def cnt(n):
    cnt = 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            cnt += 1
            if i != n // i: cnt += 1
    return cnt
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = gcd(a, b)
        return cnt(g)