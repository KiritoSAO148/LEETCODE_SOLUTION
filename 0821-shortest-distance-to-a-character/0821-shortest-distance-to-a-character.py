class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        idx = [i for i in range(len(s)) if s[i] == c]
        j = 0
        res = []
        for i in range(len(s)):
            if s[i] == c: res.append(0)
            else:
                x = 10**18
                for y in idx: x = min(x, abs(y - i))
                res.append(x)
        return res