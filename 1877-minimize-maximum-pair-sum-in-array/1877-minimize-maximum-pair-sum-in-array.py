class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = -10 ** 9
        l = 0; r = len(nums) - 1
        while l <= r:
            ans = max(ans, nums[l] + nums[r])
            l += 1
            r -= 1
        return ans