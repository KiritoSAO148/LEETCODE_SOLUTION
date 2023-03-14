class Solution:
    def sumZero(self, n: int) -> List[int]:
        a = [] * n
        a.append(0)
        for i in range(1, n // 2 + 1): 
            a.append(i)
            a.append(-i)
        if n % 2 == 0: a.pop(0)
        return a