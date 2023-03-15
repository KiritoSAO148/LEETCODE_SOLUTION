class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = {}
        for x in items1: d[x[0]] = x[1]
        for x in items2:
            if x[0] in d: d[x[0]] += x[1]
            else: d[x[0]] = x[1]
        return sorted(d.items())