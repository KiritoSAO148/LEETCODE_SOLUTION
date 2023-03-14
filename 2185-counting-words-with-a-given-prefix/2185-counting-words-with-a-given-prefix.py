class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for x in words:
            if x.startswith(pref): cnt += 1
        return cnt