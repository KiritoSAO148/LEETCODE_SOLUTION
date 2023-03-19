from collections import Counter
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        d = {}
        for x in set(nums1): d[x] = 1 + d.get(x, 0)
        for x in set(nums2): d[x] = 1 + d.get(x, 0)
        for x in set(nums3): d[x] = 1 + d.get(x, 0)
        res = []
        for x in d:
            if d[x] >= 2: res.append(x)
        return res