from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = list(dict(Counter(arr)).values())
        for x in counter:
            if counter.count(x) > 1: return False
        return True