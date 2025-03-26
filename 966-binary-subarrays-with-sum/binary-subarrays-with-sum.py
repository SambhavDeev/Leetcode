class Solution:
    def caller(self,nums,goal):
        if goal<0:
            return 0
        l=0
        cnt=0
        sumer=0
        for r in range(len(nums)):
            sumer+=nums[r]
            while sumer>goal:
                sumer-=nums[l]
                l+=1
            
            cnt+=(r-l+1)
            
        return cnt

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        a=self.caller(nums,goal)
        b=self.caller(nums,goal-1)
        return a-b

        

        