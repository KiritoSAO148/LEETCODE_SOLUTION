class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        a = [[0 for _ in range(n)] for _ in range(m)]
        for x in indices:
            r, c = x[0], x[1]
            for i in range(n): a[r][i] += 1
            for i in range(m): a[i][c] += 1
        cnt = 0
        for x in a:
            for y in x:
                if y % 2: cnt += 1
        return cnt