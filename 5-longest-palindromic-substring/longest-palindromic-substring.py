class Solution:
    def longestPalindrome(self, s: str) -> str: #twopointer
        resind=0
        reslen=0
        for i in range(len(s)):
            l=i
            r=i
            #odd length
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    residx=l
                    reslen=r-l+1

                l-=1
                r+=1
            #even length
            l=i
            r=i+1
            while l>=0 and r<len(s)and s[l]==s[r]:
                if (r-l+1)>reslen:
                    residx=l
                    reslen=r-l+1
                l-=1
                r+=1
        return s[residx:residx+reslen]