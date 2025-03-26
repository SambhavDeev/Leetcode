class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=0
        end=0
        zero=0
        maxer=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            if zero>k:
                if nums[start]==0:
                    zero-=1
                start+=1

            if zero<=k:
                currlen=(end-start+1)
                maxer=max(maxer,currlen)

            end+=1
        return maxer


        