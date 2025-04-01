class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        r=0
        word=set()
        while r<len(s):
            while s[r] in word:
                word.remove(s[l])
                l+=1
            word.add(s[r])
            res=max(res,(r-l+1))
            r+=1
        return res
