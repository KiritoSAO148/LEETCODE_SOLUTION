class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        f = [0] * (len(gain) + 1)
        f[0] = 0
        for i in range(len(gain)): f[i] = f[i - 1] + gain[i]
        return max(f)