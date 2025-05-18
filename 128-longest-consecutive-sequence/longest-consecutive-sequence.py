class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        max_len=0
        for n in num:
            if n-1 not in num:
                length=0
                while (n+length) in num:
                    length+=1
                max_len=max(length,max_len)
        return max_len
                
        
        