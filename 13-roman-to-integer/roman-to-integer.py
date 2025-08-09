class Solution:
    def romanToInt(self, s: str) -> int:
        rmn={"I":1,"V" :5,"X" : 10,"L":50,"C":100,"D":500,"M":  1000}
        res=0
        for i in range(len(s)):
            if i+1<len(s) and rmn[s[i]]< rmn[s[i+1]]:
                res-=rmn[s[i]]
            else:
                res+=rmn[s[i]]
        return res

