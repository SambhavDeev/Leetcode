class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()#left white space

        if len(s)==0:
            return 0

        ans,sign=0,1

        if s[0]=="-":
            sign=-1
            s=s[1:]
        elif s[0]=="+":
            s=s[1:]

        for c in s:
            if c.isdigit():
                ans=ans*10+int(c)

            else:
                break
        ans*=sign

        miner=-(2**31)
        maxer=2**31 - 1

        if ans>maxer:
            return maxer

        elif ans<miner:
            return miner
        else:
            return ans
