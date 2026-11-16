class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []
        res2 = []
        for i in range(len(names)):
            res.append((heights[i], names[i]))
        res = sorted(res, reverse=True)
        for i in range(len(res)):
            res2.append(res[i][1])
        return res2
        