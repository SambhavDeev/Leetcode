class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)

        ind=-1
        for i in range(n-2,-1,-1):#find the breaking point or the point where the elemnt got dip as when we check from back we see element is increasing and when we get to see element got less we mark the index
            if nums[i]<nums[i+1]:
                ind=i
                break

        if ind==-1: #this means ki last permutaion is given so we reverse it to get first permutation
            nums.reverse()
            return nums

        for i in range(n-1,ind,-1):#find the greater element than the breaking point index from back its always going to be the last index from the back only 
            if nums[i]>nums[ind]:
                nums[i],nums[ind]=nums[ind],nums[i]
                break

        
        nums[ind+1:]=reversed(nums[ind+1:])

        return nums

