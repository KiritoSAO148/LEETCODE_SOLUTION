class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [x for x in nums if x > 0]
        negative = [x for x in nums if x < 0]
        a = []
        for i in range(len(positive)):
            a.append(positive[i])
            a.append(negative[i])
        return a