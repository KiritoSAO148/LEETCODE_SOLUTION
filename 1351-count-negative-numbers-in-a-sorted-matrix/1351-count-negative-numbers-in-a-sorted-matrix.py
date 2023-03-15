def neg(n): return n < 0

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(grid)): cnt += len(list(filter(neg, grid[i])))
        return cnt