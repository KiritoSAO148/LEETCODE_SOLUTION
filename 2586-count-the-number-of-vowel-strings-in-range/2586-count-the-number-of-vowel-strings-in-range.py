def vowel(c):
        return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        cnt = 0
        for i in range(left, right + 1):
            if vowel(words[i][0]) and vowel(words[i][-1]): cnt += 1
        return cnt