class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for i in range(len(details)): 
            age = int(details[i][11] + details[i][12])
            if age > 60:
                res += 1
        return res
