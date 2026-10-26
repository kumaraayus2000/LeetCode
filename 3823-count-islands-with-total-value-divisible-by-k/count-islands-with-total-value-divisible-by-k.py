class Solution:


    def dfs(self,grid,x1,x2):
        n1 = len(grid)
        n2 = len(grid[0])

        if x1<0 or x2 <0 or x1>=n1 or x2>=n2:
            return 0

        if grid[x1][x2]==0:
            return 0

        island = grid[x1][x2]
        grid[x1][x2]=0

        directions = [
            (-1,0),
            (0,-1),
            (0,1),
            (1,0)
        ]


        for dx,dy in directions:
            new_x = x1 + dx
            new_y = x2 + dy
            island+= self.dfs(grid,new_x,new_y)

        return island

    def countIslands(self, grid: List[List[int]], k: int) -> int:
        
        n1 = len(grid)

        n2 = len(grid[0])

        count =0
        for x1 in range(n1):
            for x2 in range(n2):
                if grid[x1][x2]!=0:
                    island= self.dfs(grid,x1,x2)
                    if island%k==0:
                        count+=1

        return count