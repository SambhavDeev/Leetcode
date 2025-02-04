class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res=nums[0]
        sumer=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                sumer+=nums[i]

            else:
                sumer=nums[i]

            res=max(res,sumer)
        return res
        