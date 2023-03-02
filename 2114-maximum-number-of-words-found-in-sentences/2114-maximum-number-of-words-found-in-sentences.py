class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        m = 0
        for x in s: m = max(m, len(list(x.split())))
        return m