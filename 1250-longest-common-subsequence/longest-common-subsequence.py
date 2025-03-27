class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ind1=len(text1)-1
        ind2=len(text2)-1
        dp=[[-1]*(ind2+1) for _ in range(ind1+1)]
        def f(ind1,ind2,dp):
            if ind1<0 or ind2<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if text1[ind1]==text2[ind2]:
                dp[ind1][ind2]=1+f(ind1-1,ind2-1,dp)
            else:
                dp[ind1][ind2]=max(f(ind1-1,ind2,dp),f(ind1,ind2-1,dp))
            
            return dp[ind1][ind2]

        return f(ind1,ind2,dp)