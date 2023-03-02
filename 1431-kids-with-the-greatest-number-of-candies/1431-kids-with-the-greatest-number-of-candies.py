class Solution:
    def kidsWithCandies(self, a: List[int], k: int) -> List[bool]:
        m, res = max(a), [] * len(a)
        for x in a:
            if x + k >= m: res.append(True)
            else: res.append(False)
        return res