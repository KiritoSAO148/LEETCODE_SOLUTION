def solve(n):
    res = 0
    if n == 0: return res
    if n % 2 == 0: res += solve(n // 2) + 1
    else: res += solve(n - 1) + 1
    return res
class Solution:
    def numberOfSteps(self, num: int) -> int:
        return solve(num)