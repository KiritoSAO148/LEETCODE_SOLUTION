class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for x in nums:
            if len(str(x)) % 2 == 0: cnt += 1
        return cnt