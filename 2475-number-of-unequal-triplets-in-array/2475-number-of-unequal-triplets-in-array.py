class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]: cnt += 1
        return cnt