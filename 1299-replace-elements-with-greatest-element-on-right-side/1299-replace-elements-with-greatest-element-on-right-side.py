class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res, tmp = [-1], arr[-1]
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > tmp: tmp = arr[i]
            res.append(tmp)
        return reversed(res)