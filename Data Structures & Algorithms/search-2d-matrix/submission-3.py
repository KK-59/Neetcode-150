class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target > matrix[i][len(matrix[0])-1]:
                continue
            else:
                if len(matrix[0]) == 1:
                    if matrix[i][0] == target:
                        return True
                    else:
                        return False
                prev = 0
                low = 0
                high = len(matrix[0])-1
                while low < high: 
                    mid = (low + high) // 2               
                    if target == matrix[i][low] or target == matrix[i][high] or target == matrix[i][mid]:
                        return True
                    elif target > matrix[i][mid]:
                        low = mid
                        if low == prev:
                            return False
                    else:
                        high = mid
                        if high == prev:
                            return False
                    prev = mid
        return False