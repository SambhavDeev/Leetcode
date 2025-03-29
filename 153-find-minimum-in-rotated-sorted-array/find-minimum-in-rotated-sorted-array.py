class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        res=nums[0]
        while l<=r:
            if nums[l]<nums[r]:
                return min(nums[l],res)

            mid=(l+r)//2
            res=min(res,nums[mid])
            if nums[l]<=nums[mid]:
                l=mid+1
            else:
                r=mid-1

        return res
