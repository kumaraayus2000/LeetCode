class Solution:
    @lru_cache(None)
    def dfs(self,x:int,y:int,m:int,n:int)->int:

        if x>=m or y>=n:
            return 0

        if x==m-1 and y==n-1:
            return 1

        down = self.dfs(x+1,y,m,n)

        right = self.dfs(x,y+1,m,n)
        return down + right


    def uniquePaths(self, m: int, n: int) -> int:
        
        return self.dfs(0,0,m,n)