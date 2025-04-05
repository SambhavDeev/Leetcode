class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l=0
        cnt=0
        for i in range(len(s)):
            if l>=len(g):
                break
            if s[i]>=g[l]:
                l+=1
                cnt+=1

        return cnt
