class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = []
        for i in range(n // 2): a += nums[2 * i] * [nums[2 * i + 1]]
        return a
            