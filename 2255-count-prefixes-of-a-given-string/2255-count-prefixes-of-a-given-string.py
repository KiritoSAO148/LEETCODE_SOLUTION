class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return len([x for x in words if s.startswith(x)])