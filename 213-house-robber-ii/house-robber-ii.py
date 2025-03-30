class Solution(object):
    def search(self,nums):
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        dp=[0]*(n+1)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            pick=nums[i]+dp[i-2]
            nonpick=0+dp[i-1]
            dp[i]=max(pick,nonpick)
        return dp[n-1]
        
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return nums[0]

        lft=self.search(nums[1:])
        rght=self.search(nums[:-1])
        return max(lft,rght)

        