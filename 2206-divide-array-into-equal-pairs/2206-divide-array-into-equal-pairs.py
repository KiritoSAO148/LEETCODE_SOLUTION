from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        check = True
        d = dict(Counter(nums))
        for x in d.keys():
            if d[x] % 2:
                check = False
                break
        return check