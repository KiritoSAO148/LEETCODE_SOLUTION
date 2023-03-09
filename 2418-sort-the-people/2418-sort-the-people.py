class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a = []
        for i in range(len(names)): a.append([heights[i], names[i]])
        ans = []
        for x in sorted(a, reverse = True): ans.append(x[1])
        return ans