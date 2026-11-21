class Solution:
    def isValidSudoku(self, matrix: List[List[str]]) -> bool:
        # check rows

        rec = {} # number -> frequency

        for i in range(1, 10): 
            rec[str(i)] = 0

        for i in range(len(matrix)): 
            temp = rec.copy()
            for j in range(len(matrix[0])): 
                if matrix[i][j] != "." and temp[matrix[i][j]] > 0: 
                    return False
                elif matrix[i][j] != ".": 
                    temp[matrix[i][j]] += 1
        
                
        for i in range(len(matrix)):
            temp = rec.copy()
            for j in range(len(matrix[0])): 
                if matrix[j][i] != "." and temp[matrix[j][i]] > 0: 
                    return False
                elif matrix[j][i] != ".": 
                    temp[matrix[j][i]] += 1 
        indx = [0, 3, 6]
        for i in range(len(indx)): 
            x = indx[i]
            for j in range(len(indx)): 
                y = indx[j]
                temp = rec.copy()
                for k in range(x, x+3): 
                    for l in range(y, y+3):
                        if matrix[k][l] != "." and temp[matrix[k][l]] > 0:
                            return False
                        elif matrix[k][l] != ".": 
                            temp[matrix[k][l]] += 1 
        
        return True


        
        