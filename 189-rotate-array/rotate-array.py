class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #reversing the whole array
        n=len(nums)
        k=k%n
        nums[:]=nums[:][::-1]#reverse the whole array
        nums[:k]=nums[:k][::-1]#reverse upto k elements
        nums[k:]=nums[k:][::-1]#reverse from the k to last element
        return nums