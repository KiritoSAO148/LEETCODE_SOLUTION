class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = [0] * 101
        for x in nums: cnt[x] += 1
        s = 0
        for x in nums:
            if cnt[x] == 1: s += x
        return s