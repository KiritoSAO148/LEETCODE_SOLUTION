class Solution:
    def differenceOfSum(self, a: List[int]) -> int:
        s1, s2 = sum(a), 0
        for x in a:
            s = 0
            while x != 0:
                s += x % 10
                x //= 10
            s2 += s
        return abs(s1 - s2)