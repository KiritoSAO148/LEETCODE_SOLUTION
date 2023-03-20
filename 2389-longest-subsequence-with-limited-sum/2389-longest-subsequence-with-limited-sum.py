def bs(a, x):
    res, l, r = -1, 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] <= x:
            res = m
            l = m + 1
        else: r = m - 1
    return res

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)): f[i] = f[i - 1] + nums[i]
        res = []
        for x in queries:
            tmp = bs(f, x)
            if tmp == -1: res.append(0)
            else: res.append(tmp + 1)
        return res