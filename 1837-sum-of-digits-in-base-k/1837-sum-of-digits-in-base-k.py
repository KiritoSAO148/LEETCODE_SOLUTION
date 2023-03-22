class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = ''
        while n != 0:
            res = str(n % k) + res
            n //= k
        return sum(list(map(int, res)))