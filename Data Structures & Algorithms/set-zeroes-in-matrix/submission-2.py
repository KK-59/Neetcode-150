class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        temp = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0: 
                    for p in range(len(matrix[0])):
                        temp[i][p] = True
                    for q in range(len(matrix)):
                        temp[q][j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if temp[i][j] == True:
                    matrix[i][j] = 0


        