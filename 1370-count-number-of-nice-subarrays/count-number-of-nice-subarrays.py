class Solution:
    def call(self,nums,k):
        if k<0:
            return 0
        l=0
        curr=0
        cnt=0
        for r in range(len(nums)):
            curr+=(nums[r]%2)
            while curr>k:
                curr-=(nums[l]%2)
                l+=1
            cnt+=(r-l+1)
        return cnt       
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.call(nums,k)-self.call(nums,k-1)
        