class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for x in operations:
            if x == '+': res.append(res[-1] + res[-2])
            elif x == 'D': res.append(res[-1] * 2)
            elif x == 'C': res.pop()
            else: res.append(int(x))
        return sum(res)