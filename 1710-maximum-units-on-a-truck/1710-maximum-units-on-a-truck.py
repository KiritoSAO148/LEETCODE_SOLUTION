class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : -x[1])
        s = 0
        for i in range(len(boxTypes)):
            if boxTypes[i][0] <= truckSize:
                s += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
            elif boxTypes[i][0] > truckSize:
                s += truckSize * boxTypes[i][1]
                break
        return s