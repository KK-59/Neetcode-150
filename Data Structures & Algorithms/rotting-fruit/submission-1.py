class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    Q.append((i,j))
        def bfs(i,j, Q):
            time = 0
            while len(Q) > 0:
                for _ in range(len(Q)): 
                    (i,j) = Q[0]
                    Q.pop(0)
                    if i + 1 < len(grid) and grid[i+1][j] == 1:
                        Q.append((i+1, j))
                        grid[i+1][j] = 2
                    if i - 1 >= 0 and grid[i-1][j] == 1:
                        Q.append((i-1, j))
                        grid[i-1][j] = 2
                    if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
                        Q.append((i,j+1))
                        grid[i][j+1] = 2
                    if j - 1 >= 0 and grid[i][j-1] == 1:
                        Q.append((i,j-1))
                        grid[i][j-1] = 2
                if Q:
                    time += 1
            return time
        time = bfs(i,j,Q)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return time