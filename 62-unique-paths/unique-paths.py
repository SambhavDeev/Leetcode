class Solution:
    def uniquePaths(self, m: int, n: int) -> int:#tabukation
        dp=[[-1 for _ in range(n+1)] for _ in range(m+1)]
       
        dp[1][1]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1 and j==1:
                    dp[1][1]=1
                    continue
                up=0
                left=0
                if i>1:
                    up=dp[i-1][j]
                if j>1:
                    left=dp[i][j-1]
                
                dp[i][j]=left+up

        return dp[m][n]
        