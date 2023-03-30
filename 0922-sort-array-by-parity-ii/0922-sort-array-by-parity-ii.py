class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [x for x in nums if x % 2 == 0]
        odd = [x for x in nums if x % 2]
        res = []
        for a, b in zip(even, odd):
            res.append(a)
            res.append(b)
        return res