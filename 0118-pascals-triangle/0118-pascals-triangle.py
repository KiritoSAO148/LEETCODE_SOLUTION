class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [[0 for _ in range(numRows)] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0 or j == i: a[i][j] = 1
                else: a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
        res = []
        for i in range(len(a)):
            tmp = []
            for j in range(i + 1): tmp.append(a[i][j])
            res.append(tmp)
        return res