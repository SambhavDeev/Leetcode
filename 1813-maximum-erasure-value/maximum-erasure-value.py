class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen={}
        curr=0
        maxer=0
        left=0
        for right, val in enumerate(nums):
            while val in seen and seen[val]>=left:
                curr-=nums[left]
                left+=1
            curr+=val
            seen[val]=right
            maxer=max(curr,maxer)

        return maxer