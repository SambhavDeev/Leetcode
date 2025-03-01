class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxer=float("-inf")
        sumer=0
        #starti , endi = -1,-1

        for i in range(len(nums)):
            #if sumer=0:
                #start=i
            sumer+=nums[i]

            if sumer>maxer:
                maxer=sumer
                #starti=start , endi=i

            if sumer<0:
                sumer=0

        return maxer

        