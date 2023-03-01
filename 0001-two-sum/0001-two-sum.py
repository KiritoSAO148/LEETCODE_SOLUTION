class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)): d[nums[i]] = i
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in d and d[tmp] != i: return [i, d[tmp]]