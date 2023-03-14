class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans = ""
        for x in words:
            if x == x[::-1]:
                ans = x
                return ans
        return ans