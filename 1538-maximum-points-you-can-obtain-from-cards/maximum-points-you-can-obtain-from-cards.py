class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        lsum,rsum,maxer,rindex=0,0,0,len(nums)-1
        for i in range(k):
            lsum+=nums[i]
            maxsum=lsum
        for i in range(k-1,-1,-1):
            lsum-=nums[i]
            rsum+=nums[rindex]
            rindex-=1

            maxsum=max(maxsum,lsum+rsum)

        return maxsum
        