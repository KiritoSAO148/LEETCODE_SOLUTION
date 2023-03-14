class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        digits = []
        for x in nums:
            digit = list(map(int, str(x)))
            digits += digit
        return digits