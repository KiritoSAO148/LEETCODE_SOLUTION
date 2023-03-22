class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num = str(num); res = int(num[::-1]); ans = int(str(res)[::-1])
        return int(ans) == int(num)