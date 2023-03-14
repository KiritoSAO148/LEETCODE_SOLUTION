class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        cnt = [0] * 10001
        for x in nums: cnt[x] += 1
        for x in set(nums):
            if cnt[x] == len(nums) // 2: return x