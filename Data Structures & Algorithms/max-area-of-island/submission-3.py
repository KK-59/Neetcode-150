class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        zeros = True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    zeros = False
                    break
        if zeros:
            return 0

        def dfs(u,v):
            res = []
            for i in range(len(grid)): 
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        res.append(dfs_visit(i,j))
            # print(res)
            return max(res)
        def dfs_visit(i,j): 
            curArea = 1
            grid[i][j] = 0
            if i + 1 < len(grid) and grid[i+1][j] == 1:
                curArea += dfs_visit(i+1, j)
            if i - 1 >= 0 and grid[i-1][j] == 1:
                curArea += dfs_visit(i-1, j)
            if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
                curArea += dfs_visit(i, j+1)
            if j - 1 >= 0 and grid[i][j-1] == 1:
                curArea += dfs_visit(i, j-1)
            return curArea
        return dfs(0,0)
