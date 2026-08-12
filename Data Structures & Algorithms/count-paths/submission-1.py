class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1 or m == 1:
            return 1
        R = [[0 for _ in range(n)] for _ in range(m)]
        R[0][0] = 0
        for i in range(1,m):
            R[i][0] = 1
        for i in range(1,n):
            R[0][i] = 1

        for i in range(1, m):
            for j in range(1,n):
                R[i][j] = R[i-1][j] + R[i][j-1]
        return R[-1][-1]