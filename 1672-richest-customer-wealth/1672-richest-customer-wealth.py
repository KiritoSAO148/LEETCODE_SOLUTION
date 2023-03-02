class Solution:
    def maximumWealth(self, a: List[List[int]]) -> int:
        res = -10 ** 18
        for i in range(len(a)):
            s = sum(a[i])
            res = max(res, s);
        return res