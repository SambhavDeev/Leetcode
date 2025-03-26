class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastseen=[-1]*3
        cnt=0
        for i in range(len(s)):
            lastseen[ord(s[i])-ord('a')]=i
            cnt+=1+min(lastseen)

        return cnt