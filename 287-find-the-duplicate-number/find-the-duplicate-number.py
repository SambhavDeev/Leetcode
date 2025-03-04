class Solution:
    def findDuplicate(self, nums: List[int]) -> int:#floyd warshal fast and slow pointer
        slow=0
        fast=0
        while True:#this is stupid floyd 
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow=0
        while True:
            slow=nums[slow]
            fast=nums[fast]
            if slow==fast:
                return fast
        return -1