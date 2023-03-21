class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0; n = len(arr)
        for i in range(len(arr)):
            left, right = i, n - i - 1
            s += arr[i] * ((left // 2) + 1) * ((right // 2) + 1)
            s += arr[i] * ((left + 1) // 2) * ((right + 1) // 2)
        return s