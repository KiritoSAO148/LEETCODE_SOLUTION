from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mp = dict(Counter(arr))
        for key, val in mp.items():
            if val == 1: k -= 1
            if k == 0: return key
        return ''