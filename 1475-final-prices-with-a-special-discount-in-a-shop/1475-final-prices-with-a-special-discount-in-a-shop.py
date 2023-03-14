class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans, n = [], len(prices)
        for i in range(n - 1):
            cur, idx = prices[i], i
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    idx = j
                    break
            if idx == i: ans.append(prices[i])
            else: ans.append(prices[i] - prices[idx])
        ans.append(prices[-1])
        return ans