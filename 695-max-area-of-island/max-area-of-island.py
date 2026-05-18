class Solution:

    def dfs(self, x:int,y:int,grid:List[List[int]])->int:

        if x<0 or y<0 or x>=len(grid) or y >= len(grid[0]) or grid[x][y]==0:
            return 0

        grid[x][y]=0

        return (1 
                + self.dfs(x+1,y,grid) 
                + self.dfs(x,y+1,grid) 
                + self.dfs(x-1,y,grid) 
                + self.dfs(x,y-1,grid)
        )

        return 0


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        max1 = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    max1=max(max1,self.dfs(i,j,grid))

        
        return max1