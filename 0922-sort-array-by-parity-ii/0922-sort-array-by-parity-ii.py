class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [x for x in nums if x % 2 == 0]
        odd = [x for x in nums if x % 2]
        res = []
        for i in range(len(nums)):
            if i % 2 == 0: 
                res.append(even[0])
                even.pop(0)
            else:
                res.append(odd[0])
                odd.pop(0)
        return res