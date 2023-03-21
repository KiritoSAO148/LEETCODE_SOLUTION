class Solution:
    def pivotInteger(self, n: int) -> int:
        f = [0] * (n + 1)
        f[1] = 1
        for i in range(2, n + 1): f[i] = f[i - 1] + i
        for i in range(1, n + 1):
            if f[i] == f[n] - f[i - 1]: return i
        return -1