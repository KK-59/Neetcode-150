class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(matrix[0])):
            res.append([])
            for j in range(len(matrix)):
                res[i].append(0)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])): 
                res[j][i] = matrix[i][j]
        return res
                