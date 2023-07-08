class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        for x in words:
            res = 0
            for i in set(x):
                if i not in allowed: res += 1
            if not res: cnt += 1
        return cnt