class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[-1]*(n+1)
        dp[0]=nums[0]

        for i in range(1,n):
            pick=nums[i]
            if i>1:
                pick+=dp[i-2]

            nonpick=0+dp[i-1]
            dp[i]=max(pick,nonpick)

        return dp[n-1]
