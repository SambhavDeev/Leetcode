import math
class Solution(object):
    def binsrch(self,piles,mid):
        hrs=0
        for p in piles:
            hrs+=math.ceil(p/float(mid))
        return hrs

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        if h==len(piles):
            return max(piles)
        l=1
        r=max(piles)
        ans=r
        while l<=r:
            mid=(l+r)//2

            hr=self.binsrch(piles,mid)
            if hr<=h:
                ans=mid
                r=mid-1

            else:
                l=mid+1
        return ans