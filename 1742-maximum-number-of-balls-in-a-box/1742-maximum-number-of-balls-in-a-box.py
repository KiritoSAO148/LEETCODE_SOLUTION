from collections import defaultdict
def s(n):
    res = 0
    while n != 0:
        res += n % 10
        n //= 10
    return res
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = defaultdict(int)
        for i in range(lowLimit, highLimit + 1): d[s(i)] += 1
        return max(d.values())