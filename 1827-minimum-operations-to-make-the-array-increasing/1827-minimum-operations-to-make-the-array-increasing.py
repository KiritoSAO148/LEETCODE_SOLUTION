class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                cnt += abs(nums[i] - nums[i - 1]) + 1
                nums[i] = nums[i - 1] + 1
        return cnt