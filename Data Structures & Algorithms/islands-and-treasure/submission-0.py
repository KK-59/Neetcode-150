class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def bfs(i,j):
            Q = []
            Q.append((i,j))
            while len(Q) > 0:
                (i,j) = Q[0]
                Q.pop(0)
                if i + 1 < len(grid) and grid[i][j] + 1 < grid[i+1][j]:
                    grid[i+1][j] = grid[i][j] + 1
                    Q.append((i+1, j))
                if i - 1 >= 0 and grid[i][j] + 1 < grid[i-1][j]:
                    grid[i-1][j] = grid[i][j] + 1
                    Q.append((i-1, j))
                if j + 1 < len(grid[0]) and grid[i][j] + 1 < grid[i][j+1]:
                    grid[i][j+1] = grid[i][j] + 1
                    Q.append((i, j+1))
                if j - 1 >= 0 and grid[i][j] + 1 < grid[i][j-1]:
                    grid[i][j-1] = grid[i][j] + 1
                    Q.append((i, j-1))
                    
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs(i,j)
