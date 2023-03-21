class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        for i in range(len(arr)):
            tmp = 0
            for j in range(i, len(arr)):
                tmp += arr[j]
                if (j - i + 1) % 2 == 1: s += tmp
        return s