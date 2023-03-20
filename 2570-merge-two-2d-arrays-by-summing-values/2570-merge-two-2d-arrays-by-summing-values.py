import collections
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(int)
        for key, val in nums1: d[key] += val
        for key, val in nums2: d[key] += val
        return sorted([[key, val] for key, val in d.items()])