class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #using dutch national flag
        n=len(nums)
        l,m,h=0,0,n-1
        while m<=h:
            if nums[m]==0:
                nums[m],nums[l]=nums[l],nums[m]
                m+=1
                l+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[m],nums[h]=nums[h],nums[m]
                h-=1

        return nums