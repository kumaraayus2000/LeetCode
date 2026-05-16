class Solution:

    def dfs(self,x:int,y:int,grid:List[List[str]]):

        if x<0 or y<0 or x>len(grid)-1 or y> len(grid[0])-1 or grid[x][y]=='0':
            return

        grid[x][y]='0'

        self.dfs(x+1,y,grid)
        self.dfs(x-1,y,grid)
        self.dfs(x,y-1,grid)
        self.dfs(x,y+1,grid) 


    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])

        count =0

        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    count+=1
                    self.dfs(i,j,grid)

        
        return count
        