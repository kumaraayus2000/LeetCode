class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]* (n+1)

        dp[0]=1
        dp[1]=1

        for node in range(2,n+1):
            total =0
            for i in range(1,node+1):
                left = i-1
                right = node-i
                total += dp[left] * dp[right]
            
            dp[node]= total
        
        return dp[n]