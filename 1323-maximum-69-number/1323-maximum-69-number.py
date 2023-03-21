class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        return int(num.replace('6', '9', 1))