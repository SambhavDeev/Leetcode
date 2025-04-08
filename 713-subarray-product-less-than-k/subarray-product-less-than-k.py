class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod=1
        cnt=0
        left=0
        for right, val in enumerate(nums):
            prod*=val
            while prod >= k and left<=right:
                prod//=nums[left]
                left+=1
            cnt+=right-left+1

        return cnt