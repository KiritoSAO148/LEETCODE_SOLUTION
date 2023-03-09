class Solution:
    from itertools import permutations
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = list(permutations(nums))
        return res