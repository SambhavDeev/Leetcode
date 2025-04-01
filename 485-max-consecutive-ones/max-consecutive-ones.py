class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        l=0
        r=0
        while r<len(nums):
            if nums[r]==0:
                l=r+1
            
            cnt=max(cnt,(r-l+1))
            r+=1
        return cnt