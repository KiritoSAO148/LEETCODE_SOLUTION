class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans = ''
        for x in s.split()[:k]: ans += x + ' '
        return ans.strip()