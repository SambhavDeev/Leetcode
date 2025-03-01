class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #using dutch national flag
        n=len(nums)
        low,mid,high=0,0,n-1

        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                mid+=1
                low+=1

            elif nums[mid]==1:
                mid+=1

            else:#nums[mid]==2
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1

        return nums