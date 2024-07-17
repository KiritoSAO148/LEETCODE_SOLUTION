class Solution:
    def sortSentence(self, s: str) -> str:
        a = [word[-1] + word[:-1] for word in s.split()]
        a.sort()
        ans = ''
        for word in a:
            ans += word[1:] + ' '
        return ans[:-1]