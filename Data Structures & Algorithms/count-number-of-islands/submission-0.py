class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # run DFS and every time it goes back to the original function, increment 
        def dfs(v,e): 
            res = 0
            time = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "1":
                        res += 1
                        dfs_visit(i,j)
            return res
        def dfs_visit(i,j): 
            grid[i][j] = 0
            if i + 1 < len(grid) and grid[i+1][j] == "1":
                dfs_visit(i+1,j) 
            if i - 1 >= 0 and grid[i-1][j] == "1":
                dfs_visit(i-1,j) 
            if j + 1 < len(grid[0]) and grid[i][j+1] == "1":
                dfs_visit(i,j+1)
            if j - 1 >= 0 and grid[i][j-1] == "1":
                dfs_visit(i,j-1)
        return dfs(0,0) 




        