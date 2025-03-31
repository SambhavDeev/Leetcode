class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        ans=float("-inf")
        prefix=1
        suffix=1
        for i in range(len(nums)):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1

            prefix=prefix*nums[i]
            suffix=suffix*nums[n-i-1]
            ans=max(prefix,suffix,ans)

        return ans