def check(n):
    tmp = n
    while n != 0:
        r = n % 10
        if r == 0 or tmp % r: return False
        n //= 10
    return True
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for x in range(left, right + 1):
            if check(x): res.append(x)
        return res