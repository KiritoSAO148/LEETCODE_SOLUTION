class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        for x in set(nums):
            if x == 0: cnt = 1
        return len(set(nums)) - cnt