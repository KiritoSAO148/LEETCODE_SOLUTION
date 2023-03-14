class Solution:
    from math import gcd
    def findGCD(self, nums: List[int]) -> int:
        return gcd(max(nums), min(nums))