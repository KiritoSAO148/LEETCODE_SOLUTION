class Solution:
    from collections import Counter
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt, left = 0, 0
        d = dict(Counter(nums))
        for x in set(nums):
            if d[x] % 2 == 1:
                left += 1
                cnt += d[x] // 2
            else: cnt += d[x] // 2
        return [cnt, left]